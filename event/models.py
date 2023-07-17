from django.db import models

# Create your models here.
class Event(models.Model):
    # Atributos de la clase Event
    start_date = models.DateTimeField(null=True) #YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] lo que está entre corchetes es opcional.
    end_date = models.DateTimeField(null=True)
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

    owner = models.ForeignKey('auth.user', related_name='events') #on_delete=models.CASCADE?indica que si un usuario se elimina, todos sus fragmentos de código también se eliminarán.

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)