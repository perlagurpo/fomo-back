from rest_framework import serializers
from .models import Event

from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        #fields=('fullname','nickname') #Indicando los campos individualmente
        fields = '__all__' #todos los campos


class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', ''] #??