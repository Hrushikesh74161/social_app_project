from django.contrib import admin

from . import models


@admin.register(models.Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('uploaded_by', 'uploaded_on',)
    list_filter = ('uploaded_by', 'uploaded_on',)
    ordering = ('-uploaded_on',)