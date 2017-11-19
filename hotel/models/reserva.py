from django.db import models
from .pago import Forma_de_pago


class Reserva(models.Model):

    costoAlojamiento = models.FloatField(default=0.0)
    estado = models.BooleanField(default=False)
    tipoReserva = models.CharField(max_length=15)
    fechaIngresa = models.DateTimeField(blank=True, null=True)
    fechaReserva = models.DateTimeField(blank=True, null=True)
    fechaSalida = models.DateTimeField(blank=True, null=True)
    forma_de_pago = models.ForeignKey(Forma_de_pago)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return '%s' % (self.tipoReserva)
