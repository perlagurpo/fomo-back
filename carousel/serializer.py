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
                  'image_mobile',
                  'description_button',
                  'link_button'
                  ]