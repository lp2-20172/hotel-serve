
from django.conf.urls import url, include
from rest_framework import routers
from .views.habitacion_view import HabitacionViewSet
from .views.cliente_view import ClienteViewSet

router = routers.DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'cliente', ClienteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
