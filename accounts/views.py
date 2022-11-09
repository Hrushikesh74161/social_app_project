from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model

from .forms import ProfileEditForm
from .models import Profile


def view_profile(request, username):
    profile = get_object_or_404(Profile, username=username)
    user_model = get_user_model()
    profile_user = user_model.objects.get(username=username)
    images = profile_user.my_uploads.all()
    return render(request, 'accounts/profile.html', context={'profile': profile, 'images': images})


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