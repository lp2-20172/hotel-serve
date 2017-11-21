from django.db import models
from core.models import Person


class Cliente(models.Model):

    estado = models.CharField(max_length=11)
    datos_cliente = models.OneToOneField(Person)
    tipo_cliente = models.CharField(max_length=11)
    informacion_adicional = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % (self.datosCliente)
