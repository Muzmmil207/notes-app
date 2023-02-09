from django.db.models import Count, Sum

from .models import Label


def labels(request):
    return {
        "labels": Label.objects.filter(user=request.user)
        .values("name")
        .annotate(count_notes=Count("note"))
    }
