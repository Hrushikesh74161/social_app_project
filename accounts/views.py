from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from .forms import ProfileEditForm
from .models import Profile, FollowSystem


def view_profile(request, username):
    profile = get_object_or_404(Profile, username=username)
    profile_user = profile.user
    images = profile_user.my_uploads.all()
    try:
        follow_status = FollowSystem.objects.get(from_user=request.user, to_user=profile_user)
    except ObjectDoesNotExist:
        follow_status = None
    return render(request, 'accounts/profile.html', context={'profile': profile, 'images': images, 'follow_status': follow_status})


@login_required  # type: ignore
def edit_profile(request, username):
    profile = get_object_or_404(Profile, username=username)
    if request.user == profile.user:
        if request.method == 'POST':
            profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successfully.')
                return render(request, 'accounts/profile.html', {'profile': profile})
            else:
                messages.error(request, 'Error updating your profile.')
        else:
            profile_form = ProfileEditForm(instance=profile)

            return render(request, 'accounts/profile_update.html', {'profile_form': profile_form})
    else:
        raise PermissionDenied