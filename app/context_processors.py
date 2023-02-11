from django.db.models import Count

from .models import Label, Note


def labels(request):
    if request.user.is_authenticated:
        return {
            "labels": Label.objects.filter(user=request.user)
            .values("name")
            .annotate(count_notes=Count("note"))
        }
    return {"labels": []}


def notes_length(request):
    if request.user.is_authenticated:
        return {"notes_len": Note.objects.filter(user=request.user).count()}
    return {"notes_len": 0}
