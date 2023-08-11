from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


from .models import Event
from .serializer import EventSerializer, EventDetailSerializer, EventCreatorSerializer
from event.services import get_event_by_query_params, replace_T_and_Z


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
        queryset = get_event_by_query_params(query_params=query_params)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(paginated_queryset, many=True)
        serializer = replace_T_and_Z(serializer=serializer)
        return Response(status=200, data=serializer.data)


class EventDetailView(generics.RetrieveAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    lookup_field = 'pk'



###Pensando en usuarios creadores
class CreatorEventListCreateView(
    generics.ListCreateAPIView,                     
                          ):
    serializer_class = EventCreatorSerializer #acá tengo que hacer un serializer para los usuarios creadores
    permission_classes = [IsAuthenticated] #IsOwnerOrReadOnly ?

    def get_queryset(self):#y si no tiene eventos creados?
        return Event.objects.filter(user_creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user_creator=self.request.user)


class CreatorDetailUpdateDestroy(
    generics.UpdateAPIView, 
    generics.RetrieveDestroyAPIView
    ):
    serializer_class = EventCreatorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Event.objects.filter(user_creator=self.request.user)
        
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

        












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