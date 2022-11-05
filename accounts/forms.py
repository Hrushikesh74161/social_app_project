from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'display_picture', 'bio', 'gender', 'date_of_birth',)