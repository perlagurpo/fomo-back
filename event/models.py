from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from location.models import Location
from django.utils import timezone
import os

def image_upload_path(instance, filename):
    timestamp = timezone.now().strftime('%Y-%m-%d--%H-%M-%S')
    extension = os.path.splitext(filename)[-1]
    unique_filename = f"{timestamp}{extension}"
    return os.path.join('images', unique_filename)


class DateEvent(models.Model):
    fecha = models.DateField()

    def __str__(self):
        return str(self.fecha)


# Create your models here.
class Event(models.Model):
    TICKET_TYPES = (
        ('Entrada virtual', 'Entrada virtual'),
        ('Entrada física', 'Entrada fisica'),
        ('Entrada física y virtual', 'Entrada fisica y virtual')
    )
    start_date = models.DateTimeField(verbose_name='Inicio del evento') #YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] lo que está entre corchetes es opcional.
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='Fin del evento')
    event_name = models.CharField(max_length=255, verbose_name='Nombre del evento')
    has_ticket = models.BooleanField(null=True, blank=True, verbose_name='¿Tiene entrada?')
    ticket_price = models.IntegerField(null=True, blank=True, verbose_name='Precio')
    tickets_left = models.BooleanField(null=True, blank=True, verbose_name='¿Quedan entradas?')
    tickets_available = models.IntegerField(null=True, blank=True, verbose_name='Cantidad de entradas disponibles')
    ticket_type = models.CharField(max_length=255, choices=TICKET_TYPES, null=True, blank=True, verbose_name='Tipo de entrada', help_text='Entrada virtual, física, etc')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')
    buy_tickets = models.CharField(max_length=255, null=True, blank=True, verbose_name='Link para comprar tickets:')
    event_link = models.CharField(max_length=255, null=True, blank=True, verbose_name='Link al evento:')
    event_img = models.ImageField(max_length=255, upload_to=image_upload_path, verbose_name='Imagen del evento')
    organization_page = models.CharField(max_length=255, null=True, blank=True, verbose_name='Página organización')
    location_event = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Lugar')
    user_creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True, verbose_name='Organización')#esto no me gusta
    highlighted = models.BooleanField(default=False, verbose_name='¿Evento destacado?')#excluido del panel de creación en admin.py
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True, to_field='name', verbose_name='categoría')
    slug = models.SlugField(blank=True)
    date_to_repeat = models.ManyToManyField(DateEvent, blank=True, null=True)


    class Meta:
        ordering = ['start_date']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    @property
    def day_name_start(self):
        if self.start_date:
            # Establece idioma español
            #locale.setlocale(locale.LC_ALL, 'es_AR.utf8') #validar con el "locale -a"
            #locale.getlocale(locale.LC_TIME)
            # Formatear la fecha y obtener el nombre del día... ahora en es
            day_name_start_eng = self.start_date.strftime('%A').capitalize()
            day_name_start_es = translate_day(day_name_start_eng)
            return day_name_start_es
        return None
    

    @property
    def day_name_end(self):
        if self.start_date:
            # Establece idioma español
            #locale.setlocale(locale.LC_ALL, 'es_AR.utf8') #validar con el "locale -a"
            #locale.getlocale(locale.LC_TIME)
            # Formatear la fecha y obtener el nombre del día... ahora en es
            day_name_end_eng = self.end_date.strftime('%A').capitalize()
            day_name_end_es = translate_day(day_name_end_eng)
            return day_name_end_es
        return None
    
    @property
    def time_difference(self):
        if self.start_date and self.end_date:
            duration = self.end_date - self.start_date

            days = duration.days
            hours, remainder = divmod(duration.seconds, 3600)
            minutes, _ = divmod(remainder, 60)

            return f"{days} días, {hours} horas, {minutes} minutos"
        
        return None


    def __str__(self):
        return self.event_name
    
    def image_url(self):
        if self.event_img:
            return self.event_img.url
        return None

####No pude ponerlo en services.py por 'importaciones circulares'
def translate_day(day_in_english):
    traducciones = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }

    return traducciones.get(day_in_english, "Día no válido")



####Para cambiar el formato de la fecha en nuevo falso-atributo
# def event_date_formatted(self, obj):
    # return obj.event_date.strftime("%d-%m-%Y %H:%M")  # Formato deseado
    # event_date_formatted.short_description = 'Fecha del Evento'  # Nombre de la columna en el admin
