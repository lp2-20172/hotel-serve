from ..models.detalleVenta import Detalle_Venta
from rest_framework import serializers, viewsets
#from rest_framework import permissions
#from django.db.models import Q
#from operator import __or__ as OR
#from functools import reduce#


class Detalle_VentaSerializer(serializers.ModelSerializer):
    venta_numDoc = serializers.SerializerMethodField()
    venta_direccion = serializers.SerializerMethodField()

    class Meta:
        model = Detalle_Venta
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')

    def get_venta_numDoc(self, obj):
        return "%s " % (obj.Venta.numDoc)

    def get_venta_direccion(self, obj):
        return "%s " % (obj.Venta.direccion)


class Detalle_VentaViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Venta.objects.all()
    serializer_class = Detalle_VentaSerializer
    #permission_classes = [permissions.IsAuthenticated]
