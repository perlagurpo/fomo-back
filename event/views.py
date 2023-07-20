###views.py ES JUAN ROMÁN RIQUELME###

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from event.serializer import EventSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from event.models import Event
from rest_framework import filters
from datetime import datetime

from rest_framework import generics
from .models import Event
from .serializer import EventSerializer
from event.services import main_filters

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request): #si llega una GET request:
        if len(request.data.keys()) == 0: #si llega sin pedir filtro muestra todo
            queryset = Event.objects.all() #bbdd a qs
            serializer = EventSerializer(queryset, many=True) #transforma de obj
            return Response(serializer.data) #retorna respuesta
        
        elif len(request.data.keys()) > 0:
            return main_filters(self, request)

    @authentication_classes([SessionAuthentication])
    @permission_classes([IsAuthenticated])
    def create(self, request): #si llega un POST request:
        #create necesita auth, list no. Ver chatgpt
        user = request.user
        data = request.data
        data['user_creator'] = user
        serializer = EventSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)