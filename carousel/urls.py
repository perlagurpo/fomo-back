from django.urls import path
from .views import CarouselListView


urlpatterns = [
    path(r'', CarouselListView.as_view(), name='carousel_list_view')
]
