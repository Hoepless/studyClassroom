from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Comment
from main.tasks import comment_to_models


@receiver(post_save, sender=Comment)
def comment_to_model(sender, **kwargs):
    comment_to_models.delay()
    # post_save.connect(comment_to_model, sender=sender)

