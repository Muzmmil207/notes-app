from datetime import datetime

from app.models import Note
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError


class NotesSerializer(ModelSerializer):
    """A serializer class for note model"""

    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Note
        fields = [
            "id",
            "user",
            "label",
            "title",
            "content",
            "remind",
            "created_at",
            "updated_at",
            "url",
        ]

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if len(data["title"]) == 0 and len(data["content"]) == 0:
            raise ValidationError("finish must occur after start")
        return data

    def validate_remind(self, value):
        """
        Check that the type of note.remind is a datetime object.
        """
        if not type(value) is datetime or value != None:
            raise ValidationError("remind is not datetime object.")

        return value
