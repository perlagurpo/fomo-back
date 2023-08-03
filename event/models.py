from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime
import locale
from category.models import Category

# Create your models here.
class Event(models.Model):
    # Atributos de la clase Event
    start_date = models.DateTimeField() #YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] lo que está entre corchetes es opcional.
    end_date = models.DateTimeField(null=True, blank=True)
    event_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255, null=True, blank=True)
    has_ticket = models.BooleanField(null=True, blank=True)
    ticket_price = models.IntegerField(null=True, blank=True)
    tickets_left = models.BooleanField(null=True, blank=True)
    tickets_available = models.IntegerField(null=True, blank=True)
    buy_tickets = models.CharField(max_length=255, null=True, blank=True)
    event_link = models.CharField(max_length=255, null=True, blank=True)
    event_img = models.ImageField(max_length=255, upload_to='images/')
    organization_page = models.CharField(max_length=255, null=True, blank=True)
    event_location = models.CharField(max_length=255)
    user_creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)#esto no me gusta
    highlighted = models.BooleanField(default=False)#excluido del panel de creación en admin.py
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True, to_field='name')

    class Meta:
        ordering = ['start_date']

    @property
    def day_name_start(self):
        if self.start_date:
            # Establece idioma español
            locale.setlocale(locale.LC_ALL, 'es_AR.utf8') #validar con el "locale -a"
            locale.getlocale(locale.LC_TIME)
            # Formatear la fecha y obtener el nombre del día... ahora en es
            return self.start_date.strftime('%A').capitalize()
        return None
    
    @property
    def day_name_end(self):
        if self.start_date:
            # Establece idioma español
            locale.setlocale(locale.LC_ALL, 'es_AR.utf8') #validar con el "locale -a"
            locale.getlocale(locale.LC_TIME)
            # Formatear la fecha y obtener el nombre del día... ahora en es
            return self.end_date.strftime('%A').capitalize()
        return None


    def __str__(self):
        return self.event_name
    
    def image_url(self):
        if self.event_img:
            return self.event_img.url
        return None


