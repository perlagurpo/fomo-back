# Generated by Django 4.2.2 on 2023-08-12 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='image_mobile',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]