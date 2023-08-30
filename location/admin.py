from django.contrib import admin
from location.models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    #exclude = ('google_maps_link',)


# Register your models here.
admin.site.register(Location, LocationAdmin)
