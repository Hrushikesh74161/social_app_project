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
    username = models.CharField(max_length=150)
    email = models.EmailField('Email Address', editable=False)
    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, blank=True, null=True)

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
        # return reverse('accounts/<username>', args=[])