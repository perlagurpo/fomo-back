#####Acá van las funciones para que las llame de otros lugares y quede más prolijo###
import datetime
from .models import Event
from django.db.models import Q, F



def get_event_by_query_params(query_params):
    if len(query_params) == 0:
        queryset = get_today_event()
    else:
        queryset = filter_queryset_by_query_params(filters_data=query_params)
    return queryset

####Si no se usan filtros de búsqueda:
def get_today_event():
    now = datetime.datetime.now()
    queryset = Event.objects.filter(end_date__gt=now).order_by(F('start_date').asc(nulls_last=True))
    return queryset

####Si se usan filtros de búsqueda:
def filter_queryset_by_query_params(filters_data):
    queryset = Event.objects.all()
    if 'start_date' in filters_data.keys():
        queryset = date_filter(
            start_date=filters_data['start_date'],
            end_date=filters_data.get('end_date', None),
            query_set=queryset
        )
    if 'event_name' in filters_data.keys():
        queryset = event_name_contain_filter(data=filters_data, query_set=queryset)
    return queryset



def date_filter(
        query_set,
        start_date:datetime.datetime,
        end_date: datetime.datetime =None
):

    date_formated = datetime.datetime.strptime(start_date, '%d-%m-%Y')
    date_start = datetime.datetime.combine(date_formated, datetime.time.min)
    date_end = datetime.datetime.combine(date_formated, datetime.time.max)
    if end_date:
        end_date_formated = datetime.datetime.strptime(end_date, '%d-%m-%Y')
        date_end = datetime.datetime.combine(end_date_formated, datetime.time.max)
    event_filter_qs = query_set.filter(start_date__range=[date_start, date_end])
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
        if item['end_date'] is not None:
            item['end_date'] = item['end_date'].replace('T', ' ').replace('Z', '')
    return serializer


