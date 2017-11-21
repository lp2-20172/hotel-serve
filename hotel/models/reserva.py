from django.db import models
from .pago import Forma_de_pago


class Reserva(models.Model):

    costo_alojamiento = models.FloatField(default=0.0)
    estado = models.BooleanField(default=False)
    tipo_reserva = models.CharField(max_length=15)
    fecha_ingresa = models.DateTimeField(blank=True, null=True)
    fecha_reserva = models.DateTimeField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    forma_de_pago = models.ForeignKey(Forma_de_pago)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return '%s' % (self.tipoReserva)
