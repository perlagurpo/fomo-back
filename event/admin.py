from django.contrib import admin
from .models import Event, DateEvent
from django.forms.widgets import SelectMultiple
from datetime import datetime
class EventAdmin(admin.ModelAdmin):
    actions = ['highlighted_true', 'highlighted_false', 'repeat_event']
    list_display = ('event_name', 'highlighted', 'start_date')
    search_fields = ('event_name', 'user_creator')
    exclude = ["tickets_available", "organization_page", "slug", "event_link"]

    class Meta:
        widgets = {
            'date_to_repeat': SelectMultiple(attrs={'size': '50'}),
        }

    def repeat_event(self, request, queryset):
        for event in queryset:
            for date in event.date_to_repeat.all():
                fecha_inicio = datetime.combine(date.fecha, datetime.min.time())
                fecha_fin = datetime.combine(date.fecha, datetime.max.time())
                event_qs = Event.objects.filter(slug__contains=event.slug.split('-')[0], start_date__range=(fecha_inicio, fecha_fin))
                if not event_qs.exists():
                    try:
                        new_event = Event()
                        new_event.event_name = event.event_name
                        new_event.has_ticket = event.has_ticket
                        new_event.ticket_price = event.ticket_price
                        new_event.tickets_left = event.tickets_left
                        new_event.tickets_available = event.tickets_available
                        new_event.ticket_type = event.ticket_type
                        new_event.description = event.description
                        new_event.event_link = event.event_link
                        new_event.buy_tickets = event.buy_tickets
                        new_event.event_img = event.event_img
                        new_event.organization_page = event.organization_page
                        new_event.location_event = event.location_event
                        new_event.user_creator = event.user_creator
                        new_event.highlighted = event.highlighted
                        new_event.category = event.category
                        new_event.highlighted = event.highlighted
                        new_date = date.fecha
                        new_date = datetime(new_date.year, new_date.month, new_date.day, event.start_date.hour, event.start_date.minute, 0)
                        difference = event.start_date - event.end_date
                        new_event.start_date = new_date
                        new_event.end_date = new_date - difference
                        new_event.save()
                    except Exception as error:
                        print(error)

    def highlighted_true(self, request, queryset):
        for event in queryset:
            event.highlighted = True
            event.save()

    def highlighted_false(self, request, queryset):
        for event in queryset:
            event.highlighted = False
            event.save()

    highlighted_true.short_description = "Marcar como destacado"
    highlighted_false.short_description = "Desmarcar como destacado"
    repeat_event.short_description = "Repetir evento"


admin.site.register(Event, EventAdmin)
admin.site.register(DateEvent)
