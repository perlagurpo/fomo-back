from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailView(generics.RetrieveAPIView):
    #queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
###############Para traer sólo el objeto que busca y no todo el queryset########
    def get_object(self):
        # Obtener el valor de la clave primaria (pk) de la URL de la solicitud
        pk = self.kwargs['pk']

        # Obtener el objeto Event por su clave primaria
        category = Category.objects.get(pk=pk)

        return category
