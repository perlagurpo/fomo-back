from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from event.serializer import EventSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from event.models import Event
from datetime import datetime


from .models import Event
from .serializer import EventSerializer
from event.services import main_filters, replace_T_and_Z

from rest_framework.decorators import authentication_classes, permission_classes
#para el refactor?
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q, F
from rest_framework.pagination import PageNumberPagination
class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    pagination_class = UserPagination
    #ordering = ['-start_date']
    
    def list(self, request): #si llega una GET request:
        now = datetime.now()
        if len(request.query_params.keys()) == 0: 
            queryset = Event.objects.filter(
                Q(start_date__gt=now) | (Q(start_date__lt=now) & Q(end_date__gt=now))
            ).order_by(F('start_date').asc(nulls_last=True))
        else:
            queryset = main_filters(self, request)

        paginated_queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(paginated_queryset, many=True)
        serializer = replace_T_and_Z(serializer=serializer)
        return self.get_paginated_response(serializer.data)


    #@authentication_classes([SessionAuthentication])
    #@permission_classes([IsAuthenticated])
    def create(self, request): #si llega un POST request:
        #create necesita auth, list no. Ver chatgpt
        #user = request.user
        data = request.data
        # if user is not 'AnonymusUser':
        #     data['user_creator'] = user # "Incorrect type. Expected pk value, received AnonymousUser."
        # if request.data['image'] is not None:
        #     image = data.pop('image')
        #     image_path = ''#guardar imagen en carpeta estatica
        #     data['image'] = image_path

        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)