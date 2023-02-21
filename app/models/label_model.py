import uuid

from django.db import models
from django.db.models import CASCADE, Model
from django.utils.translation import gettext as _

from .user_model import User


class Label(Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("ID"),
    )
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.DateTimeField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_("Name"),
        help_text=_("A label name."),
    )

    def __str__(self):
        return f"{self.user.username} | {self.name}"
