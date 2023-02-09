from django.db.models import Count

from .models import Label, Note


def labels(request):
    return {
        "labels": Label.objects.filter(user=request.user)
        .values("name")
        .annotate(count_notes=Count("note"))
    }


def notes_length(request):
    return {"notes_len": Note.objects.filter(user=request.user).count()}
