# Generated by Django 4.2.2 on 2023-09-07 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import event.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0004_alter_location_options_location_coordinates'),
        ('category', '0004_alter_category_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Inicio del evento')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Fin del evento')),
                ('event_name', models.CharField(max_length=255, verbose_name='Nombre del evento')),
                ('has_ticket', models.BooleanField(blank=True, null=True, verbose_name='¿Tiene entrada?')),
                ('ticket_price', models.IntegerField(blank=True, null=True, verbose_name='Precio')),
                ('tickets_left', models.BooleanField(blank=True, null=True, verbose_name='¿Quedan entradas?')),
                ('tickets_available', models.IntegerField(blank=True, null=True, verbose_name='Cantidad de entradas disponibles')),
                ('ticket_type', models.CharField(blank=True, help_text='Entrada virtual, física, etc', max_length=255, null=True, verbose_name='Tipo de entrada')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('buy_tickets', models.CharField(blank=True, max_length=255, null=True, verbose_name='Comprar tickets:')),
                ('event_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Link al evento:')),
                ('event_img', models.ImageField(max_length=255, upload_to=event.models.image_upload_path, verbose_name='Imagen del evento')),
                ('organization_page', models.CharField(blank=True, max_length=255, null=True, verbose_name='Página organización')),
                ('highlighted', models.BooleanField(default=False, verbose_name='¿Evento destacado?')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category', to_field='name', verbose_name='categoría')),
                ('location_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.location', verbose_name='Lugar')),
                ('user_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Organización')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'ordering': ['start_date'],
            },
        ),
    ]
