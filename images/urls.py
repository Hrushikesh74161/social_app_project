from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    path('upload/', views.ImageUploadView.as_view(), name='image_upload'),
    path('<uuid:pk>', views.ImageDetailView.as_view(), name='image_detail'),
]