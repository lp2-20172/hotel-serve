
from django.conf.urls import url, include
from rest_framework import routers
from .views.habitacion_view import HabitacionViewSet
from .views.cliente_view import ClienteViewSet
from .views.detalleVenta_view import Detalle_VentaViewSet
from .views.area_view import AreaViewSet
from .views.docType_view import Doc_TypeViewSet
from .views.pago_view import Forma_de_pagoViewSet
from .views.reserva_view import ReservaViewSet
from .views.trabajador_view import TrabajadorViewSet
from .views.venta_view import VentaViewSet

router = routers.DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'detalleVenta', Detalle_VentaViewSet)
router.register(r'area', AreaViewSet)
router.register(r'docType', Doc_TypeViewSet)
router.register(r'pago', Forma_de_pagoViewSet)
router.register(r'reserva', ReservaViewSet)
router.register(r'trabajador', TrabajadorViewSet)
router.register(r'venta', VentaViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
