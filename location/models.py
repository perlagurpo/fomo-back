from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name='Lugar')
    address = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name='Dirección')
    coordinates = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name='Coordenadas')

    def __str__(self):
        return self.name
    
    @property
    def google_maps_link(self):
        if self.coordinates:
            return f'http://maps.google.com/maps?q={self.coordinates}'
        else:
            return None

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'