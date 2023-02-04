from app.models import *
from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import api_view, permission_classes
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
