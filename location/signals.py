from django.db.models.signals import pre_save
from django.dispatch import reciever
from .models import Location

@reciever(pre_save, sender=Location)
def generate_google_maps_link(sender, instance, **kwargs):
    print("HOLAAAAAA")
    instance.google_maps_link=f'http://maps.google.com/maps?q={self.coordinates}'