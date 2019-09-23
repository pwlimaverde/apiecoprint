from django.db import models
from datetime import datetime


class RegistroOp(models.Model):
    orcamento = models.IntegerField(blank=False, null=False)
    cliente = models.CharField(max_length=300, blank=False, null=False)
    servico = models.TextField(blank=False, null=False)
    quant = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    entrada = models.DateField(blank=False, null=False)
    vendedor = models.CharField(max_length=100, blank=False, null=False)
    op = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.op) + ' - ' + self.cliente
