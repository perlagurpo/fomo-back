# Generated by Django 4.2.2 on 2023-08-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Nombre'),
        ),
    ]
