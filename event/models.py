from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date

# Create your models here.
class Event(models.Model):
    # Atributos de la clase Event
    start_date = models.DateTimeField(null=True) #YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] lo que está entre corchetes es opcional.
    #day_of_week_start = models.CharField(max_length=10, blank=True, null=True)  # Atributo para almacenar el día del evento
    end_date = models.DateTimeField(null=True)
    #day_of_week_end = models.CharField(max_length=10, blank=True, null=True)
    event_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255, null=True)
    has_ticket = models.BooleanField(null=True)
    ticket_price = models.IntegerField(null=True)
    tickets_left = models.BooleanField(null=True)
    tickets_available = models.IntegerField(null=True)
    buy_tickets = models.CharField(max_length=255, null=True)
    event_link = models.CharField(max_length=255, null=True)
    event_img = models.CharField(max_length=255, null=True)
    organization_page = models.CharField(max_length=255, null=True)
    event_location = models.CharField(max_length=255, null=True)
    user_creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)#esto no me gusta
    highlighted = models.BooleanField(default=False)


    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return self.event_name
    
    def get_weekday_name(self):
        if self.start_date:
            return self.start_date.strftime('%A')
        return None
    

""" 
    owner = models.ForeignKey('auth.user', related_name='events') #on_delete=models.CASCADE?indica que si un usuario se elimina, todos sus fragmentos de código también se eliminarán.

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) """