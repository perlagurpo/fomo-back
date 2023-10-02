from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'