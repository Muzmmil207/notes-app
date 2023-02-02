from app.models import Label, Note, User
from rest_framework.serializers import ModelSerializer


class NotesSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
