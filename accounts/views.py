from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .forms import ProfileEditForm
from .models import Profile


@login_required
def view_profile(request, username):
    profile = get_object_or_404(Profile, username=username)
    return render(request, 'accounts/profile.html', context={'profile': profile})


@login_required
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