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
    # #Acá estoy poniendo los @property que no se incluyen solos cuando uso fields = '__all__'
    # day_name_start = serializers.SerializerMethodField(source='get_day_name_start')
    # #day_name_end = serializers.SerializerMethodField(source='get_day_name_end')
    # #day_name_end = end_date_check()
    # # location_name = serializers.SerializerMethodField(source='get_location_name')
    # # location_address = serializers.SerializerMethodField(source='get_location_address')
    # # location_maps_url = serializers.SerializerMethodField(source='get_location_maps_url')

    # #Intento de validadores por si end_date o event_location vienen vacíos o sólo devuelven el ID
    # def end_date_check(self):
    #     if self.end_date:
    #         day_name_end = serializers.SerializerMethodField(source='get_day_name_end')
    #     return day_name_end
    
    # def location_check(self):
    #     if self.location_event is (isinstance(self.location_event, int) or not None or not self.location_event != ""):
    #     #if self.location_event is not None and not isinstance(self.location_event, int) and self.location_event != "":            
    #         location_name = serializers.SerializerMethodField(source='get_location_name')
    #         location_address = serializers.SerializerMethodField(source='get_location_address')
    #         location_maps_url = serializers.SerializerMethodField(source='get_location_maps_url')
    # class Meta:
    #     model=Event
    #     fields = '__all__'





    # def get_day_name_start(self, obj):
    #     return obj.day_name_start

    # def get_day_name_end(self, obj):
    #     return obj.day_name_end
    
    
    # def get_location_name(self, obj):
    #     return obj.location_event.name
    
    # def get_location_address(self, obj):
    #     return obj.location_event.address
    
    # def get_location_maps_url(self, obj):
    #     return obj.location_event.google_maps_link
    

    location_event = LocationSerializer()    
    
    class Meta:
        model=Event
        fields = [
                "id",
                "day_name_start",
                "day_name_end",
                "start_date",
                "end_date",
                "event_name",
                "has_ticket",
                "ticket_price",
                "tickets_left",
                "tickets_available",
                "ticket_type",
                "description",
                "buy_tickets",
                "event_link",
                "event_img",
                "organization_page",
                "highlighted",
                "slug",
                "location_event",
                "user_creator",
                "category",
                "location_event",
        ]