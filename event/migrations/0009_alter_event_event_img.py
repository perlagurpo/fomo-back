# Generated by Django 4.2.2 on 2023-08-25 02:35

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_alter_event_buy_tickets_alter_event_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_img',
            field=models.ImageField(max_length=255, upload_to=event.models.image_upload_path, verbose_name='Imagen del evento'),
        ),
    ]