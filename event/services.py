from datetime import datetime
from event.serializer import EventSerializer
from rest_framework import filters
from .models import Event
from .serializer import EventSerializer
from rest_framework.response import Response

def filtro_fecha_exacta(data, query_set):
    filters = data 

    if 'start_date' in filters.keys():
        start_date = filters['start_date']
        print(start_date)
        if type(start_date) == list:
            date_1 = start_date[0]
            date_2 = start_date[1]
            date_1 = datetime.strptime(date_1, '%d-%m-%Y')
            date_2 = datetime.strptime(date_2, '%d-%m-%Y')
            event_filter_qs = query_set.filter(start_date__range=[date_1, date_2])
        else:
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