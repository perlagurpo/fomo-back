from rest_framework import serializers
from .models import Event
from .models import Location

from django.contrib.auth.models import User

#Este Serializer usa el EventListView
class EventSerializer(serializers.ModelSerializer):
    coordinates_maps = serializers.SerializerMethodField(source='get_maps_google_link')
    
    def get_maps_google_link(self, obj):
        if obj.location.coordinates:
            return obj.location_coordinates.maps_google_link
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
            #'location_coordinates'
            'location_name',
            #'maps_google_link',
            'coordinates_maps',

        ]
        #todos los campos


class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', ''] #??

class EventDetailSerializer(serializers.ModelSerializer):
    day_name_start = serializers.SerializerMethodField(source='get_day_name_start')
    day_name_end = serializers.SerializerMethodField(source='get_day_name_end')
    coordinates_maps = serializers.SerializerMethodField(source='get_maps_google_link')

    class Meta:
        model=Event
        fields = '__all__'
    
    def get_day_name_start(self, obj):
        return obj.day_name_start

    def get_day_name_end(self, obj):
        return obj.day_name_end
    
    def get_maps_google_link(self, obj):
        if obj.location.coordinates:
            return obj.location_coordinates.maps_google_link