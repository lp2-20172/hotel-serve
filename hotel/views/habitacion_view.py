from ..models.habitacion import Habitacion
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class HabitacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habitacion
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'is_staff')


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(tipoHabitacion__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
