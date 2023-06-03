from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from event.serializer import EventSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from event.models import Event

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Event.objects.all() #bbdd
        serializer = EventSerializer(queryset, many=True) #transforma de obj
        return Response(serializer.data) #retorna respuesta
