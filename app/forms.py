from django.forms import ModelForm

from .models.user_model import User
from .models.notes_model import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
