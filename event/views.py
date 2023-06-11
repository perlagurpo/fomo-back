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
        if len(request.data.keys()) == 0: #si llega sin pedir filtro muestra todo
            
            queryset = Event.objects.all() #bbdd
            serializer = EventSerializer(queryset, many=True) #transforma de obj
            return Response(serializer.data) #retorna respuesta
        
        if len(request.data.keys()) > 0:

            filters = request.data
            event_filter_qs = Event.objects.filter(start_date=filters['start_date']) #los filtros tienen uno o varios parámetros de entrada que siempre son los atributos del modelo en formato string

        """
        ###IMPORTANTE: Creo que esta forma primero pide toda la BBDD y después filtra... medio al pedo.
        if len(request.data.keys()) > 0:
            filters = request.data
            
            # Crear una lista de consultas (Q objects) dinámicamente
            queries = [Q(**{key: value}) for key, value in filters.items()]
            
            # Combinar las consultas utilizando operador OR
            query = queries.pop()
            for item in queries:
                query |= item
            
            # Aplicar el filtro al queryset
            queryset = queryset.filter(query)
        
        serializer = EventSerializer(queryset, many=True)
        """
        serializer = EventSerializer(event_filter_qs, many=True) #transforma de obj
        return Response(serializer.data) #retorna respuesta
    
    def create(self, request): #si llega un POST request:
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

    
