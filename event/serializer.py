from rest_framework import serializers
from .models import Event
from location.serializer import LocationSerializer

from django.contrib.auth.models import User

#Este Serializer usa el EventListView
class EventSerializer(serializers.ModelSerializer):
    location_event = LocationSerializer()
    class Meta:
        model=Event
        #fields=('fullname','nickname') #Indicando los campos individualmente
        fields = [
            'id',
            'start_date',
            'end_date',
            'day_name_start',
            'day_name_end',
            'event_name',
            'event_img',
            'image_url',
            'ticket_price',
            'highlighted',
            'category',
            'time_difference',
            'location_event',
            'slug',
        ]
        #todos los campos


class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', ''] #??

class EventDetailSerializer(serializers.ModelSerializer):
    #Acá estoy poniendo los @property que no se incluyen solos cuando uso fields = '__all__'
    day_name_start = serializers.SerializerMethodField(source='get_day_name_start')
    #day_name_end = serializers.SerializerMethodField(source='get_day_name_end')
    
    def end_date_check(self):
        if self.end_date:
            day_name_end = serializers.SerializerMethodField(source='get_day_name_end')

    
    def location_check(self):
        if self.location_event:
            location_name = serializers.SerializerMethodField(source='get_location_name')
            location_address = serializers.SerializerMethodField(source='get_location_address')
            location_maps_url = serializers.SerializerMethodField(source='get_location_maps_url')
    class Meta:
        model=Event
        fields = '__all__'
    
    def get_day_name_start(self, obj):
        return obj.day_name_start

    def get_day_name_end(self, obj):
        return obj.day_name_end
    
    
    def get_location_name(self, obj):
        return obj.location_event.name
    
    def get_location_address(self, obj):
        return obj.location_event.address
    
    def get_location_maps_url(self, obj):
        return obj.location_event.google_maps_link