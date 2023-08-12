from .models import Carousel
from rest_framework import serializers

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = [
                  'order',
                  'name',
                  'description', 
                  'image_short',
                  'description_button',
                  'link_button'
                  ]