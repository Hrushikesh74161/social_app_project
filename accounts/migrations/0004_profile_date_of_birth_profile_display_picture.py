# Generated by Django 4.1.3 on 2022-11-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='display_picture',
            field=models.ImageField(default='users/dp/default_profile.jpeg', upload_to='users/dp/', verbose_name='Picture'),
        ),
    ]