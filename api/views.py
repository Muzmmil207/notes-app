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
    mixins.DestroyModelMixin,
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
        return user.note_set.all()


class NoteDetails(generics.GenericAPIView):
    # queryset = Note.objects.all().annotate()
    # serializer_class = NotesSerializer
    def get(self, request, pk):
        note = Note.objects.get(id=pk)
        serializer = NotesSerializer(note)
        return Response(serializer.data)
