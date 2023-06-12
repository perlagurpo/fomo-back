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

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request): #si llega una GET request:
        print('request:',request)##request: <rest_framework.request.Request: GET '/event/event/'>
        print('request.data',request.data)# imprime {} porque la request no viene con filtros?
        if len(request.data.keys()) == 0: #si llega sin pedir filtro muestra todo
            print('vacío')
            queryset = Event.objects.all() #bbdd a qs
            serializer = EventSerializer(queryset, many=True) #transforma de obj
            return Response(serializer.data) #retorna respuesta



        if len(request.data.keys()) > 0:
            print('req data keys',request.data.keys())
            filters = request.data #        filters = request.query_params?
            """
            filters_list = ['event_name', 'event_type', 'ticket_price', 'event_link]  
            if filters.keys() in filters_list:
                event_filter_qs = Event.objects.filter(event_name=filters['event_name'])
                          serializer = EventSerializer(event_filter_qs, many=True) #transforma de obj
                print('serializer.data', serializer.data)
                return Response(serializer.data) #retorna respuesta       
"""
            print('filters.keys', filters)
            if 'event_name' in filters.keys():
                event_filter_qs = Event.objects.filter(event_name=filters['event_name'])
                print('event_filter_qs', event_filter_qs)
                serializer = EventSerializer(event_filter_qs, many=True) #transforma de obj
                print('serializer.data', serializer.data)
                return Response(serializer.data) #retorna respuesta                
            elif "event_type" in filters.keys():
                event_filter_qs = Event.objects.filter(event_type=filters['event_type'])
                serializer = EventSerializer(event_filter_qs, many=True) #transforma de obj
                return Response(serializer.data) #retorna respuesta                
            elif "ticket_price" in filters.keys():
                event_filter_qs = Event.objects.filter(ticket_price=filters['ticket_price'])
                serializer = EventSerializer(event_filter_qs, many=True) #transforma de obj
                return Response(serializer.data) #retorna respuesta                
            elif "event_link" in filters.keys():    
                event_filter_qs = Event.objects.filter(event_link=filters['event_link'])            
                serializer = EventSerializer(event_filter_qs, many=True) #transforma de obj
                return Response(serializer.data) #retorna respuesta
        
    def create(self, request): #si llega un POST request:
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

    
