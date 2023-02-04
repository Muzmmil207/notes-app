from django.contrib import admin

from .models.user_model import User
from .models.label_model import Label
from .models.notes_model import Note

admin.site.register(User)
admin.site.register(Note)
admin.site.register(Label)
