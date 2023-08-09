# Djagno imports
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Local imports
from event import views

urlpatterns = [
    path(r'', views.EventListView.as_view(), name='event_list'),
    path(r'<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path(r'create/', views.CreatorEventListCreateView.as_view(), name='event_create'),
    path(r'update-destroy', views.CreatorDetailUpdateDestroy.as_view(), name='event_update_destroy')

]

# Configuración para servir imágenes en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)