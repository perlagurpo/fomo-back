from django.db import models

from event.models import image_upload_path


class Carousel(models.Model):

    name = models.CharField(max_length=255, verbose_name='Nombre')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    image = models.ImageField(upload_to=image_upload_path, verbose_name='Imagen')
    image_mobile = models.ImageField(upload_to=image_upload_path, null=True, blank=True, verbose_name='Imagen mobile')
    description_button = models.CharField(max_length=255, blank=True, null=True, verbose_name='Descripción del botón')
    link_button = models.CharField(max_length=255, blank=True, null=True, verbose_name='Link del botón')
    order = models.IntegerField(help_text='Este numero se utiliza para determinar el orden del carrousel. '
                                          'Menor numero, mayor prioridad.', verbose_name='Orden')
    active = models.BooleanField(null=False, default=False, verbose_name='Activo')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    
    def image_short(self):
        if self.image:
            return self.image.url
        return None

    def image_short_mobile(self):
        if self.image_mobile:
            return self.image_mobile.url
        return None
    

    class Meta:
        verbose_name = 'Carrusel'
        verbose_name_plural = 'Carruseles'