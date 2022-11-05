from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    email = models.EmailField('Email Address', blank=False, unique=True)


class Profile(models.Model):
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_picture = models.ImageField('Picture', upload_to='users/dp/', default='users/dp/default_profile.jpeg')
    username = models.CharField(max_length=150)
    email = models.EmailField('Email Address', editable=False)
    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.username}'

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.username)])