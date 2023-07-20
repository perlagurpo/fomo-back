#####Acá van las funciones para que las llame de otros lugares y quede más prolijo###

from datetime import datetime
from event.serializer import EventSerializer
from rest_framework import filters
from .models import Event
from .serializer import EventSerializer
from rest_framework.response import Response

def main_filters(self, request):
            queryset = Event.objects

            filters = request.data

            if 'start_date' in filters.keys():
                queryset = date_filter(data=filters, query_set=queryset)

            if 'end_date' in filters.keys():
                pass
                #queryset = event_duration(data=filters, query_set=queryset)

            if 'event_name' in filters.keys():
                queryset = event_name_contain_filter(data=filters, query_set=queryset) 

            if 'event_type' in filters.keys():
                queryset = event_type_contain_filter(data=filters, query_set=queryset)

            if 'has_ticket' in filters.keys():
                queryset = has_ticket_yes_filter(data=filters, query_set=queryset)

            serializer = EventSerializer(queryset, many=True)
            if 'start_date' in filters.keys():
                serializer = replace_T_and_Z(serializer)

            return Response(serializer.data)          


def date_filter(data, query_set):
    """Si la request tiene el atributo 'start_date' y este tiene como valor una lista(#EJ: "start_date":["01-01-2001", "01-01-2005"]) la función entiende que recibe un rango de fechas y aplica un filtro.
    Si la request.data tiene como valor una sola fecha realiza un filtro estricto devolviendo los eventos de la BBDD que tienen esa fecha.

    Args:
        data (dict or dict list): request.data
        query_set (qs): queryset ya filtrado o no.

    Returns:
        object collection: el queryset filtrado.
    """
    if 'start_date' in data.keys():          
        start_date = data['start_date']
        if type(start_date) == list: #por si evento de varios días
            date_1 = start_date[0]
            date_2 = start_date[1]
            date_1 = datetime.strptime(date_1, '%d-%m-%Y')
            date_2 = datetime.strptime(date_2, '%d-%m-%Y')
            event_filter_qs = query_set.filter(start_date__range=[date_1, date_2])
        else: #para fecha exacta
            fecha_start = data['start_date']
            fecha_start_obj = datetime.strptime(fecha_start, '%d-%m-%Y')
            event_filter_qs = query_set.filter(start_date=fecha_start_obj)
        return event_filter_qs

""" def event_duration(data, query_set, duration_input, more_or_less_or_equal):
    if 'start_date' and 'end_date' in data.keys():
        start_date = data['start_date']
        end_date = data['end_date']
        duration = start_date - end_date
        if more_or_less_or_equal == 'more':

        if more_or_less_or_equal == 'more':
        if more_or_less_or_equal == 'more':

        print(duration)
    return str(duration) """

def event_name_contain_filter(data, query_set):
    """Recibe la request.data y si tiene atributo 'event_name' devuelve todos los eventos de la bbdd que -contengan- el valor del atributo en su 'event_name'.

    Args:
        data (dict): request.data
        query_set (qs): queryset ya filtrado o no.

    Returns:
        object collection: el queryset filtrado.
    """
    if 'event_name' in data.keys():
        event_name = data['event_name']
        event_filter_qs = query_set.filter(event_name__icontains=event_name)        
        return event_filter_qs

def event_type_contain_filter(data, query_set):
    if 'event_type' in data.keys():
        event_type = data['event_type']
        event_filter_qs = query_set.filter(event_type__icontains=event_type)        
        return event_filter_qs
    
def has_ticket_yes_filter(data, query_set): #me devuelve lista vacía
    if 'has_ticket' in data.keys():
        if 'has_ticket' == True:
            event_filter_qs = query_set.filter(has_ticket=True)
            return event_filter_qs

def replace_T_and_Z(serializer):
    """Reemplaza la T (time) y la Z (zone) del formato datetime por un espacio y nada respectivamente.  

    Args:
        serializer (_type_): _description_

    Returns:
        serializer object: _description_
    """    
    for item in serializer.data:
        if item['start_date'] is not None:
            item['start_date'] = item['start_date'].replace('T', ' ').replace('Z', '')
            return serializer

