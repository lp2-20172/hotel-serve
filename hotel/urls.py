
from django.conf.urls import url, include
from rest_framework import routers
from .views.habitacion_view import HabitacionViewSet
from .views.cliente_view import ClienteViewSet
from .views.detalleVenta_view import DetalleVentaViewSet

router = routers.DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'detalleVenta', DetalleVentaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
