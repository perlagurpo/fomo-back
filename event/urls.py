from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from event.views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='event')

urlpatterns = [
    path('event/', include(router.urls)),
]

# Configuración para servir imágenes en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


