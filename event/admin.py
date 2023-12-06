from django.contrib import admin
from .models import Event, DateEvent
from django.forms.widgets import SelectMultiple

class EventAdmin(admin.ModelAdmin):
    actions = ['highlighted_true', 'highlighted_false']
    list_display = ('event_name', 'highlighted', 'start_date')
    search_fields = ('event_name', 'user_creator')
    exclude = ["tickets_available", "organization_page", "slug", "event_link"]

    class Meta:
        widgets = {
            'date_to_repeat': SelectMultiple(attrs={'size': '50'}),
        }

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

admin.site.register(Event, EventAdmin)
admin.site.register(DateEvent)
