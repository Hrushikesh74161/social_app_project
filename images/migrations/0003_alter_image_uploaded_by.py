# Generated by Django 4.1.3 on 2022-11-08 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0002_alter_image_alt_text_alter_image_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_uploads', to=settings.AUTH_USER_MODEL),
        ),
    ]
