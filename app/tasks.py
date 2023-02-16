from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from notes.celery import app

from .models import Note


@shared_task(bind=True)
def dump_context(self, user_email, note_id, title, content):
    subject = "~%s~" % title
    message = render_to_string(
        "mails/note-reminder.html",
        {
            "title": title,
            "content": content,
        },
    )
    send_mail(
        subject,
        message,
        "l@1.com",
        [user_email],
        fail_silently=False,
    )

    print("Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}".format(self.request))

    Note.objects.filter(id=note_id).update(remind=None)

    return 1
