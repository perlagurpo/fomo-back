from rest_framework import viewsets, generics, mixins
from datetime import datetime
from rest_framework.response import Response

from .models import Event
from .serializer import EventSerializer, EventDetailSerializer
from event.services import get_event_by_query_params, replace_T_and_Z
from django.db.models import Q, F
from rest_framework.pagination import PageNumberPagination


class EventPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class EventListView(generics.GenericAPIView):
    serializer_class = EventSerializer
    pagination_class = EventPagination  
    queryset = Event.objects.all()

    def get(self, request):
        query_params = request.query_params
        print(query_params)
        queryset = get_event_by_query_params(query_params=query_params)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(paginated_queryset, many=True)
        serializer = replace_T_and_Z(serializer=serializer)
        return Response(status=200, data=serializer.data)


class EventDetailView(generics.RetrieveAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    lookup_field = 'pk'




# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# class CreateEventView(generics.CreateAPIView):
#     serializer_class = EventSerializer


#     def create(self, request):
#         #create necesita auth, list no. Ver chatgpt
#         #user = request.user
#         data = request.data
#         # if user is not 'AnonymusUser':
#         #     data['user_creator'] = user # "Incorrect type. Expected pk value, received AnonymousUser."
#         # if request.data['image'] is not None:
#         #     image = data.pop('image')
#         #     image_path = ''#guardar imagen en carpeta estatica
#         #     data['image'] = image_path

#         serializer = EventSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)