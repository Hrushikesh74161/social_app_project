from django.urls import path

from .views import view_profile, edit_profile

urlpatterns = [
    path('<str:username>/', view_profile, name='profile'),
    path('<str:username>/edit/', edit_profile, name='profile_edit'),
]