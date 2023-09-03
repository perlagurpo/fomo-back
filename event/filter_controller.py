#####Acá van las funciones para que las llame de otros lugares y quede más prolijo###
import datetime
from .models import Event
from django.db.models import Q, F


class FilterController(object):

    def __init__(self, params):
        self.queryset = Event.objects
        self.params = params
        self.apply_filters()

    def get_queyset(self):
        return self.queryset

    def do_nothing(*args, **kwargs):
        pass

    def apply_filters(self):
        for param in self.params.keys():
            function = getattr(self, f'{param}_filter', self.do_nothing)
            function(**self.params)

    def start_date_filter(
            self,
            start_date: datetime.datetime,
            end_date: datetime.datetime = None
    ):
        date_formated = datetime.datetime.strptime(start_date, '%d-%m-%Y')
        date_start = datetime.datetime.combine(date_formated, datetime.time.min)
        date_end = datetime.datetime.combine(date_formated, datetime.time.max)
        if end_date:
            end_date_formated = datetime.datetime.strptime(end_date, '%d-%m-%Y')
            date_end = datetime.datetime.combine(end_date_formated, datetime.time.max)
        event_filter_qs = self.queryset.filter(start_date__range=[date_start, date_end])
        return event_filter_qs

    def event_name_filter(self, event_name):
        """Recibe la request.data y si tiene atributo 'event_name' devuelve todos los eventos de la bbdd que -contengan- el valor del atributo en su 'event_name'."""
        print(event_name)
        self.queryset = self.queryset.filter(event_name__icontains=event_name)

    def category_filter(self, category):
        if type(category) is str:
            self.queryset = self.queryset.filter(category=category)
        elif type(category) is list:
            print("SI=?")
            self.queryset = self.queryset.filter(category__in=category)

    def free_filter(self, free):
            if free.lower() == 'true':
                # Para mi aca solo tiene que ser ticket_price=0
                self.queryset = self.queryset.filter(Q(ticket_price=0) | Q(ticket_price__isnull=True))
            elif free.lower() == 'false':
                self.queryset = self.queryset.exclude(Q(ticket_price=0) | Q(ticket_price__isnull=True))



