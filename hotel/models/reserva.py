from django.db import models
from core.models import Person


class Reserva(models.Model):

    costo_alojamiento = models.FloatField(default=0.0)
    estado = models.BooleanField(default=False)
    tipo_reserva = models.CharField(max_length=15)
    fecha_ingresa = models.DateTimeField(blank=True, null=True)
    fecha_reserva = models.DateTimeField(auto_now_add=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    person = models.ForeignKey(Person)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return '%s' % (self.tipo_reserva)
