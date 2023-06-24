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

from rest_framework import generics
from .models import Event
from .serializer import EventSerializer

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
            #print('req data keys',request.data.keys())
            filters = request.data 
            ###Filtro estricto###
            filters_list = ['event_name', 'event_type', 'ticket_price', 'event_link']  #filtros permitidos
            
            filters_match = [] #lista vacía de coincidencias entre filtros pedidos en la request y filtros permitidos
 
            for filtr in filters_list: #para cada elemento de filtros permitidos
                if filtr in filters.keys(): #si el elemento está en la request
                    filters_match.append(filtr) #se agrega a la lista de coincidencias

                if filters_match: #si tiene elementos
                    event_filter_qs = Event.objects #creamos consulta base
                    for filtro in filters_match: #para cada filtro de la lista de coincidencias pedidos-permitidos
                        event_filter_qs = event_filter_qs.filter(**{filtro: filters.get(filtro)}) #El operador ** se utiliza en Python para desempaquetar un diccionario y pasar sus elementos como argumentos de palabras clave a una función.

                    serializer = EventSerializer(event_filter_qs, many=True)
                    return Response(serializer.data)
               
    def create(self, request): #si llega un POST request:
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

    
