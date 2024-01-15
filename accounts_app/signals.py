from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
    post_delete,
    pre_delete
)

from accounts_app.models import (
    User,
    Profile
)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()


@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    profile = instance.profile
    profile.delete()