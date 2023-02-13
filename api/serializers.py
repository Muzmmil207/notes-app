from datetime import datetime

from app.models import Label, Note
from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
    ValidationError,
)


class NotesSerializer(ModelSerializer):
    """A serializer class for Note model"""

    url = serializers.CharField(source="get_absolute_url", read_only=True)
    label = serializers.StringRelatedField()

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
        if value and type(value) is not datetime:
            raise ValidationError("remind is not datetime object.")

        return value


class LabelsSerializer(ModelSerializer):
    """A serializer class for Label model"""

    notes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Label
        fields = ["user", "name", "notes", "id"]
