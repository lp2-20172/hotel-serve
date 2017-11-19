from ..models.detalleVenta import DetalleVenta
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class DetalleVentaSerializer(serializers.ModelSerializer):
    venta_numDoc = serializers.SerializerMethodField()
    venta_direccion = serializers.SerializerMethodField()

    class Meta:
        model = DetalleVenta
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')

    def get_venta_numDoc(self, obj):
        return "%s " % (obj.Venta.numDoc)

    def get_venta_direccion(self, obj):
        return "%s " % (obj.Venta.direccion)


class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(producto__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
