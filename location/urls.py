from django.urls import path
from django.conf import settings

from location.views import LocationListView, LocationDetailView


urlpatterns = [
    path(r'', LocationListView.as_view(), name='location_list_view'),
    path(r'<int:pk>/', LocationDetailView.as_view(), name='location_detail_view')
]
