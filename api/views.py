from app.models import *
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import NotesSerializer


@api_view(["GET"])
def get_routes(request, format=None):
    return Response(
        {
            "all user notes": reverse("notes_list", request=request, format=format),
        }
    )


class NotesList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        request.data["user"] = request.user.id
        data = request.data
        serializer = NotesSerializer(data=data)
        if serializer.is_valid() and len(data["title"]) > 0 or len(data["content"]) > 0:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        queryset = user.note_set.all().order_by("-created_at", "-updated_at")
        search_query = self.request.query_params.get("search")

        if search_query is not None:
            queryset = queryset.filter(
                Q(Q(title__iexact=search_query) | Q(title__icontains=search_query))
                | Q(content__icontains=search_query)
            )

        return queryset


class NoteDetails(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Note.objects.all()
    queryset.filter
    serializer_class = NotesSerializer
    lookup_field = "id"

    def get(self, request, id):
        return self.retrieve(request)

    def post(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
