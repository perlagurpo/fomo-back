from .models import Banner
from rest_framework import serializers

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
                  'order',
                  'name',
                  'description', 
                  'image_short',
                  'image_short_mobile',
                  'description_button',
                  'link_button'
                  ]