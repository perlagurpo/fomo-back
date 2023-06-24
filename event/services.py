from datetime import datetime
from event.serializer import EventSerializer
from rest_framework import filters
from .models import Event
from .serializer import EventSerializer
from rest_framework.response import Response

def filtro_fecha_exacta(data, query_set):
    filters = data 

    if 'start_date' in filters.keys():
        fecha_start = filters['start_date']
        fecha_start_obj = datetime.strptime(fecha_start, '%d-%m-%Y')
        event_filter_qs = query_set.filter(start_date=fecha_start_obj)
        return event_filter_qs

def filtro_event_name_contain(data, query_set):
    filters = data

    if 'event_name' in filters.keys():
        event_nombre = filters['event_name']
        event_filter_qs = query_set.filter(event_name__icontains=event_nombre)        
        return event_filter_qs