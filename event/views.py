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
from event.services import main_filters, replace_T_and_Z

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django.shortcuts import render


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request): #si llega una GET request:
        now = datetime.now()
        if len(request.query_params.keys()) == 0: #si llega sin pedir filtro muestra todo
            queryset = Event.objects.filter(start_date__gte=now) #bbdd a qs
            #queryset = queryset.filter(Q(start_date__lte=now) & Q(end_date__gte=now))
            #queryset = queryset.order_by('start_date')
        else:
            queryset = main_filters(self, request)

        serializer = EventSerializer(queryset, many=True) #transforma de obj
        serializer = replace_T_and_Z(serializer=serializer)
        return Response(serializer.data) #retorna respuesta


    #@authentication_classes([SessionAuthentication])
    #@permission_classes([IsAuthenticated])
    def create(self, request): #si llega un POST request:
        #create necesita auth, list no. Ver chatgpt
        user = request.user
        data = request.data
        #data['user_creator'] = user # "Incorrect type. Expected pk value, received AnonymousUser."

        #image = data.pop('image')
        #image_path = ''#guardar imagen en carpeta estatica
        #data['image'] = image_path

        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)