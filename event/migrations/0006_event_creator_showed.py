# Generated by Django 4.2.2 on 2023-08-09 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_remove_event_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='creator_showed',
            field=models.CharField(blank=True, default=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL), max_length=255, null=True),
        ),
    ]
