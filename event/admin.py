from django.contrib import admin
from .models import Event
from django import forms



class EventAdmin(admin.ModelAdmin):

    list_display = ('event_name', 'user_creator', 'start_date')
    search_fields = ('event_name', 'user_creator')

    def get_form(self, request, obj=None, **kwargs):
        form = super(EventAdmin, self).get_form(request, obj, **kwargs)
        
        # Si el objeto existe y has_ticket es False
        if obj and not obj.has_ticket:
            # Desactivar los campos relacionados con tickets
            for field_name in ['ticket_price', 'tickets_left', 'tickets_available', 'ticket_type', 'buy_tickets']:
                form.base_fields[field_name].disabled = True
                form.base_fields[field_name].required = False

                # Establecer valores predeterminados para los campos
                if field_name in ['ticket_price', 'tickets_available']:
                    form.base_fields[field_name].initial = None
                elif field_name == 'tickets_left':
                    form.base_fields[field_name].initial = False
                else:
                    form.base_fields[field_name].initial = ""

        return form


admin.site.register(Event, EventAdmin)