from django.forms import ModelForm

from .models import Label, Note, User


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
