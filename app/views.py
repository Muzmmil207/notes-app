from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from .decorators import is_not_authenticated
from .forms import LabelForm, NoteForm, RegistrationForm, UserLoginForm
from .models import Note


class HomeView(TemplateView):
    template_name = "main-page.html"


@login_required
def single_note_view(request, pk):
    note = get_object_or_404(Note, id=pk, user=request.user)
    form = NoteForm(instance=note)

    context = {"id": pk, "form": form}
    return render(request, "single-note.html", context=context)


@login_required
def new_note(request):
    form = NoteForm()
    context = {"form": form}

    return render(request, "create-new-note.html", context=context)


@login_required
def new_label(request):
    form = LabelForm()
    if request.method == "POST":
        form = LabelForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect("new-label")
    context = {"form": form}
    return render(request, "create-new-label.html", context=context)


@is_not_authenticated
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist.")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home-page")
        else:
            messages.error(request, "email or password is incorrect.")

    return render(
        request,
        "registration/login.html",
    )


def logout_view(request):
    logout(request)
    return redirect("login")


@is_not_authenticated
def register_view(request):
    form = RegistrationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account successfully created.")
            return redirect("login")

    context = {"form": form}
    return render(request, "registration/register.html", context)
