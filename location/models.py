from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name='Lugar')
    address = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name='Dirección')
    coordinates = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name='Coordenadas')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '¿Lugare?'
        verbose_name_plural = '¿Lugares?'

    @property
    def maps_google_link(self):
        return f'http://maps.google.com/maps?q={self.coordinates}'
