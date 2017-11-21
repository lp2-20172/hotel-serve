from ..models.reserva import Reserva
from rest_framework import serializers, viewsets


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    #permission_classes = [permissions.IsAuthenticated]
