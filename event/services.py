#####Acá van las funciones para que las llame de otros lugares y quede más prolijo###

from datetime import datetime
from event.serializer import EventSerializer
from rest_framework import filters
from .models import Event
from .serializer import EventSerializer
from rest_framework.response import Response

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
        if type(start_date) == list:
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

def ticket_price_order(data, query_set): #ANDA
    if 'ticket_price' in data.keys():
        event_filter_qs = query_set.order_by('-ticket_price')#si hiciera 'ticket_price' el ordenamiento sería descendente
        return event_filter_qs
    else:
        return query_set
####debería ser###
def ticket_price_order_button(data, query_set, asc=True): #Cómo pido el parámetro asc?
    if 'ticket_price' in data.keys():
        if asc == False:
            event_filter_qs = query_set.order_by('-ticket_price')#si hiciera 'ticket_price' el ordenamiento sería descendente
            return event_filter_qs
        else:
            event_filter_qs = query_set.order_by('ticket_price')
    else:
        return query_set



""" def ticket_price_order(data, query_set):
    if 'ticket_price' in data:
        order_by_field = 'ticket_price' if data['ticket_price'] == 'asc' else '-ticket_price'
        return query_set.order_by(order_by_field)
    else:
        return query_set """