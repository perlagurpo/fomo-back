from rest_framework import generics

from .models import Location
from .serializer import LocationSerializer


class LocationListView(generics.ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationDetailView(generics.RetrieveAPIView):
    serializer_class = LocationSerializer
    lookup_field = 'pk'
    def get_object(self):
        pk = self.kwargs['pk']

        category = Location.objects.get(pk=pk)

        return category