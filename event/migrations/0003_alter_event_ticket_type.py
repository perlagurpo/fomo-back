# Generated by Django 4.2.2 on 2023-10-02 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ticket_type',
            field=models.CharField(blank=True, choices=[('virtual', 'Entrada virtual'), ('fisica', 'Entrada física')], help_text='Entrada virtual, física, etc', max_length=255, null=True, verbose_name='Tipo de entrada'),
        ),
    ]