from django.urls import path
from django.conf import settings

from category.views import CategoryListView, CategoryDetailView


urlpatterns = [
    path(r'', CategoryListView.as_view(), name='category_list_view'),
    path(r'<int:pk>/', CategoryDetailView.as_view(), name='category_detail_view')
]


