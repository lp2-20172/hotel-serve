from ..models.pago import Pago
from rest_framework import serializers, viewsets


class PagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pago
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    #permission_classes = [permissions.IsAuthenticated]
