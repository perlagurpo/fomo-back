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
from event.services import date_filter, event_name_contain_filter, replace_T_and_Z

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request): #si llega una GET request:
        if len(request.data.keys()) == 0: #si llega sin pedir filtro muestra todo
            queryset = Event.objects.all() #bbdd a qs
            serializer = EventSerializer(queryset, many=True) #transforma de obj
            return Response(serializer.data) #retorna respuesta
        
        ###filtranga#################
        queryset = Event.objects

        if len(request.data.keys()) > 0:
            filters = request.data

            if 'start_date' in filters.keys():
                queryset = date_filter(data=filters, query_set=queryset)

            if 'event_name' in filters.keys():
                queryset = event_name_contain_filter(data=filters, query_set=queryset) 

            #Agregar filtros de orden EJ: queryset = MiModelo.objects.order_by("-fecha")

            serializer = EventSerializer(queryset, many=True)
            serializer = replace_T_and_Z(serializer)

            return Response(serializer.data)               

    def create(self, request): #si llega un POST request:
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)