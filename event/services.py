#####Acá van las funciones para que las llame de otros lugares y quede más prolijo###
import datetime
import math

from .models import Event
from django.db.models import Q, F
from event.filter_controller import FilterController

def get_event_by_query_params(query_params):
    if len(query_params) == 0 or query_params.keys() == {'page':1}.keys():
        qs = get_today_event()
    else:
        qs = FilterController(params=query_params).get_queyset()
    structure = {
        "count" : len(qs),
        "count_total_page": math.ceil(len(qs)/10),
        "actual_page": query_params.get("page", None)
    }
    return structure, qs



def get_today_event():
    now = datetime.datetime.now()
    queryset = Event.objects.filter(
        Q(end_date__gt=now) | Q(end_date__isnull=True, start_date__gt=now)
    ).order_by(F('start_date').asc(nulls_last=True))
    return queryset


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


