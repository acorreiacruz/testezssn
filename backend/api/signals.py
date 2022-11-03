from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, User)
def user_post_delete():
    ...