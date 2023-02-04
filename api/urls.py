from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("all-notes", views.NotesList.as_view(), name="notes_list"),
    path("", views.get_routes),
]

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
