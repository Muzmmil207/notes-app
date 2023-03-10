from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home-page"),
    path("note-<str:pk>/", views.single_note_view, name="single-note"),
    path("create-new-note", views.new_note, name="new-note"),
    path("create-new-label", views.new_label, name="new-label"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
]
