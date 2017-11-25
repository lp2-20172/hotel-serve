from django.db import models


class Habitacion(models.Model):

    estado = models.BooleanField(default=False)
    numero = models.CharField(max_length=15)
    piso = models.CharField(max_length=10)
    precio_diario = models.FloatField(default=0.0)
    tipo_habitacion = models.CharField(max_length=60)
    foto = models.ImageField(blank=True)
    caracteristicas = models.TextField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return '%s' % (self.tipo_habitacion)
