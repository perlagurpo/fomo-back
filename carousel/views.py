from django.shortcuts import render
from rest_framework import generics

from .serializer import CarouselSerializer
from .models import Carousel

# Create your views here.
class CarouselListView(generics.ListAPIView):
    serializer_class = CarouselSerializer
    queryset = Carousel.objects.filter(active=True).order_by('order')