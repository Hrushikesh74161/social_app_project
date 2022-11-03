from django.dispatch import receiver
from allauth.account.signals import user_signed_up

from .models import Profile


@receiver(user_signed_up)
def create_profile_when_user_signed_up(sender, request, user, **kwargs):
    profile = Profile.objects.create(
        user=user,
        username=user.username,
        email=user.email,
    )
    profile.save()