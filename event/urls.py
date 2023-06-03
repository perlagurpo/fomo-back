from django.urls import path, include
from rest_framework.routers import DefaultRouter

from event.views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='event')

urlpatterns = [
    path('event/', include(router.urls)),
]

