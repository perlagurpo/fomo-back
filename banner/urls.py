from django.urls import path
from .views import BannerListView


urlpatterns = [
    path(r'', BannerListView.as_view(), name='banner_list_view')
]
