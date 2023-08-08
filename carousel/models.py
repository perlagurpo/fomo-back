from django.db import models

# Create your models here.
class Carousel(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    description_button = models.CharField(max_length=255, blank=True, null=True)
    link_button = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(help_text='Este numero se utiliza para determinar el orden del carrousel. '
                                          'Menor numero, mayor prioridad.')
    active = models.BooleanField(null=False, default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    
    def image_short(self):
        if self.image:
            return self.image.url
        return None
