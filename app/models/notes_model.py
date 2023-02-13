import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CASCADE, Model
from django.urls import reverse
from django.utils.translation import gettext as _

from .label_model import Label
from .user_model import User


class Note(Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("ID"),
    )
    user = models.ForeignKey(User, on_delete=CASCADE)
    label = models.ForeignKey(
        Label,
        on_delete=CASCADE,
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=135,
        blank=True,
        null=True,
        verbose_name=_("Title"),
        help_text=_("A title for the note."),
    )
    content = RichTextField(
        verbose_name=_("Content"),
        blank=True,
        null=True,
    )
    remind = models.DateTimeField(
        verbose_name=_("Reminder"),
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("single-note", kwargs={"pk": self.id})

    def __str__(self):
        return f"{self.user.email} | {self.title}"
