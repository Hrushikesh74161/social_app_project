from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, ProfileEditForm
from .models import Profile, FollowSystem


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    add_form = CustomUserCreationForm
    list_display = ('username', 'email', 'is_staff',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'gender')
    ordering = ('username',)
    form = ProfileEditForm


@admin.register(FollowSystem)
class FollowSystemAdmin(admin.ModelAdmin):
    list_filter = ('from_user', 'to_user',)