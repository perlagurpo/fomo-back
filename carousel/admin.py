from django.contrib import admin
from .models import Carousel
# Register your models here.

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'order')

admin.site.register(Carousel, CarouselAdmin)