import uuid

from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models import CASCADE, Model
from django.utils.translation import gettext as _

from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Label(Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("ID"),
    )
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_("Name"),
        help_text=_("A label name."),
    )

    def __str__(self):
        return f"{self.user.username} | {self.name}"


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

    def __str__(self):
        return f"{self.user.email} | {self.title}"
