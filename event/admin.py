from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'user_creator', 'start_date')
    search_fields = ('event_name', 'user_creator')

admin.site.register(Event, EventAdmin)