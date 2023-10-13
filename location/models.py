from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Lugar')
    address = models.CharField(max_length=255, unique=True, verbose_name='Dirección')
    coordinates = models.CharField(max_length=255, unique=True, verbose_name='Coordenadas')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.coordinates:
            self.coordinates = self.coordinates.replace(" ", "")
        super(Location, self).save(*args, **kwargs)
    
    @property
    def google_maps_link(self):
        if self.coordinates:
            return f'http://maps.google.com/maps?q={self.coordinates}'
        else:
            return None

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'