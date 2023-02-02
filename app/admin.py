from django.contrib import admin

from .models import Label, Note, User

admin.site.register(User)
admin.site.register(Note)
admin.site.register(Label)
