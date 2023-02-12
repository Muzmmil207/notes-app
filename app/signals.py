from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Note
from .tasks import dump_context


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Note)
def reminder(sender, instance=None, created=False, **kwargs):
    if instance.remind is not None:

        dump_context.apply_async(
            (instance.user.email, instance.id, instance.title, instance.content),
            eta=instance.remind,
        )
