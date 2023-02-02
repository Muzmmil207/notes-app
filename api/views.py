from app.models import *
from django.shortcuts import render
from rest_framework import generics, mixins, viewsets

from .serializers import NotesSerializer


class NotesList(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = NotesSerializer

    def get(self, request):

        return self.list(request)

    def get_queryset(self):
        user = self.request.user
        return user.note_set.all()


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all().annotate()
    serializer_class = NotesSerializer
