from django.shortcuts import render
from rest_framework import generics

from .serializer import BannerSerializer
from .models import Banner

# Create your views here.
class CarouselListView(generics.ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.filter(active=True).order_by('order')