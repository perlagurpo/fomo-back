from rest_framework import serializers
from .models import Event

from django.contrib.auth.models import User

#Este Serializer usa el EventListView
class EventSerializer(serializers.ModelSerializer):
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
            'event_location',
            'ticket_price',
            'highlighted',
            'category',
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

    class Meta:
        model=Event
        fields = '__all__'
    
    def get_day_name_start(self, obj):
        return obj.day_name_start

    def get_day_name_end(self, obj):
        return obj.day_name_end
    
class EventCreatorSerializer(serializers.ModelSerializer):

    model = Event
    fields = [
        'start_date',
        'end_date',
        'event_name',
        'has_ticket',
        'ticket_price',
        'tickets_available',
        'buy_tickets',
        'event_link',
        'event_img',
        'organization_page',
        'event_location',
        'user_creator',
        'creator_showed',
    ]