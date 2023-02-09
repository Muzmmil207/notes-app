from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.forms import ModelForm

from .models import Note, User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )


class RegistrationForm(ModelForm):
    first_name = forms.CharField(
        label="Enter First Name", min_length=4, max_length=150, help_text="Required"
    )
    last_name = forms.CharField(
        label="Enter Last Name", min_length=4, max_length=150, help_text="Required"
    )
    email = forms.CharField(
        max_length=50,
        help_text="Required",
        error_messages={"required": "Sorry, you will need an email"},
    )
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "first name"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "last name"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "E-mail"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Repeat password"}
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match")
        return cd["password1"]

    def unique_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Please use another Email, this is already taken")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            "label",
            "title",
            "remind",
            "content",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["remind"].widget.attrs.update({"class": "form-element", "placeholder": ""})
        self.fields["label"].widget.attrs.update({"class": "form-element", "placeholder": ""})
        self.fields["title"].widget.attrs.update({"class": "form-element", "placeholder": ""})
        self.fields["content"].widget.attrs.update({"class": "form-element", "placeholder": ""})
