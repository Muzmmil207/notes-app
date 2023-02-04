from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import NoteForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "main-page.html"


def single_note_view(request, pk):
    form = NoteForm()
    context = {"id": pk, "form": form}
    return render(request, "single-note.html", context=context)


def new_note(request):
    form = NoteForm()
    context = {"form": form}
    return render(request, "create-new-note.html", context=context)
