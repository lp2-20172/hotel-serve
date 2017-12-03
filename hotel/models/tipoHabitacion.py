from django.db import models


class Tipo_Habitacion(models.Model):

    nombre = models.CharField(max_length=60)
    foto = models.ImageField(blank=True)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return '%s' % (self.nombre)
