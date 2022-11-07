# Generated by Django 4.1.3 on 2022-11-07 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image', models.ImageField(upload_to='users/uploads/')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('alt_text', models.CharField(blank=True, max_length=125)),
                ('liked_users', models.ManyToManyField(blank=True, related_name='liked_images', to=settings.AUTH_USER_MODEL)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
