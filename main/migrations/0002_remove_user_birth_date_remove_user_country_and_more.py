# Generated by Django 5.0.6 on 2024-07-10 04:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.CreateModel(
            name='SocialMedial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('url', models.URLField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
