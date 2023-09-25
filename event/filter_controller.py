#####Acá van las funciones para que las llame de otros lugares y quede más prolijo###
import datetime
from .models import Event
from django.db.models import Q, F
from typing import List


# Pajarok, la idea de esto es que la proxima vez que se quiera agregar un filtro solo se tiene que definir
# la funcion con el formato {nombre_de_atributo}_filter y ya se va a ejectuar solo en caso de que el parametro venga
class FilterController(object):

    def __init__(self, params):
        self.queryset = Event.objects
        self.params = params
        self.apply_filters()

    def get_queyset(self):
        return self.queryset

    def apply_filters(self):
        for param in self.params.keys():
            try:
                function = getattr(self, f'{param}_filter')
                function(**self.params)
            except AttributeError:
                print(f"filtro para {param} no existe")
            except Exception as error:
                print(error)

    def start_date_filter(
            self,
            start_date: List[datetime.datetime],
            end_date: List[datetime.datetime] = None,
            **kwargs
    ):
        start_date = start_date[0]
        date_formated = datetime.datetime.strptime(start_date, '%d-%m-%Y')
        date_start = datetime.datetime.combine(date_formated, datetime.time.min)
        if end_date:
            end_date = end_date[0]
            end_date_formated = datetime.datetime.strptime(end_date, '%d-%m-%Y')
            date_end = datetime.datetime.combine(end_date_formated, datetime.time.max)
        else:
            date_end = datetime.datetime.combine(date_formated, datetime.time.max)

        self.queryset = self.queryset.filter(start_date__range=[date_start, date_end])

    def event_name_filter(self, event_name, **kwargs):
        event_name = event_name[0]
        self.queryset = self.queryset.filter(event_name__icontains=event_name)

    def category_filter(self, category, **kwargs):
        category = category[0].split(',')
        self.queryset = self.queryset.filter(category__in=category)

    def free_filter(self, free, **kwargs):
        free = free[0]
        if free.lower() == 'true':
            # Para mi aca solo tiene que ser ticket_price=0
            self.queryset = self.queryset.filter(Q(ticket_price=0) | Q(has_ticket=False))
        elif free.lower() == 'false':
            self.queryset = self.queryset.exclude(Q(ticket_price=0) | Q(has_ticket=True))



