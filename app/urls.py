from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home-page"),
    path("<str:pk>/", views.single_note_view, name="single-note"),
    path("create-new-note", views.new_note, name="new-note"),
]
