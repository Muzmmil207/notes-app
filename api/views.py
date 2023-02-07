from app.models import *
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

        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        return user.note_set.all().order_by("-created_at", "-updated_at")


class NoteDetails(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Note.objects.all().annotate()
    serializer_class = NotesSerializer
    lookup_field = "id"

    def get(self, request, id):
        return self.retrieve(request)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
