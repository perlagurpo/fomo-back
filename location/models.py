from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True, unique=True)
    

    def __str__(self):
        return self.name