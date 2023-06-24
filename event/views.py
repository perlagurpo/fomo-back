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
from event.services import filtro_fecha_exacta, filtro_event_name_contain

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request): #si llega una GET request:
        #print('request:',request)##request: <rest_framework.request.Request: GET '/event/event/'>
        #print('request.data',request.data)# imprime {} porque la request no viene con filtros?
        if len(request.data.keys()) == 0: #si llega sin pedir filtro muestra todo
            #print('vacío')
            queryset = Event.objects.all() #bbdd a qs
            serializer = EventSerializer(queryset, many=True) #transforma de obj
            return Response(serializer.data) #retorna respuesta
        
        ###filtranga#################
        queryset = Event.objects

        if len(request.data.keys()) > 0:
            filters = request.data

            if 'start_date' in filters.keys():
                queryset = filtro_fecha_exacta(data=filters, query_set=queryset)

            if 'event_name' in filters.keys():
                queryset = filtro_event_name_contain(data=filters, query_set=queryset) 

            serializer = EventSerializer(queryset, many=True)
            estardei = serializer.data

            for item in estardei:
                if item['start_date'] is not None:
                   item['start_date'] = item['start_date'].replace('T', ' ').replace('Z', '')


            print(estardei)
            return Response(serializer.data)               

           
               
    def create(self, request): #si llega un POST request:
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)