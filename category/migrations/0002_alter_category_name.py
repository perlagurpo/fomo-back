# Generated by Django 4.2.2 on 2023-08-02 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]