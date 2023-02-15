from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.get_routes),
    path("all-notes", views.NotesList.as_view(), name="notes_list"),
    # path("labels/<str:id>", views.NotesByLabel.as_view(), name="labels"),
    path("single-notes/<str:id>", views.NoteDetails.as_view(), name="single_note"),
]
urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json", "html"])

router = DefaultRouter()
router.register(r"labels", views.NotesByLabel, basename="label")
urlpatterns += router.urls
