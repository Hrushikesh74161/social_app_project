import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse


class Image(models.Model):
    image = models.ImageField(upload_to='users/uploads/',)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    caption = models.TextField(verbose_name='Caption', blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True, db_index=True)
    alt_text = models.CharField(verbose_name='Alternate Text', max_length=125, blank=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_images', blank=True)

    def __str__(self):
        return f'Image by {self.uploaded_by.username}'

    def get_absolute_url(self):
        return reverse('images:image_detail', args=[str(self.pk)])