from celery import shared_task
from django.core.mail import send_mail


@shared_task
def comment_to_models():
    send_mail(
        "You got comment!",
        "Check classroom someone left comment",
        "test@gmail.com",
        ['kanybek.abay@gmail.com'],
        fail_siently=False
    )
