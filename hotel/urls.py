
from django.conf.urls import url, include
from rest_framework import routers
from .views.habitacion_view import HabitacionViewSet
from .views.cliente_view import ClienteViewSet
from .views.detalleVenta_view import Detalle_VentaViewSet
from .views.area_view import AreaViewSet

router = routers.DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'detalleVenta', Detalle_VentaViewSet)
router.register(r'area', AreaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
