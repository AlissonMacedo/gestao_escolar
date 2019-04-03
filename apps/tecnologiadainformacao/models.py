from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.urls import reverse
from secretaria.models import SalaDeAula

class projetor(models.Model):
    numerodeserie = models.CharField(max_length=100, null=True, blank=True)
    nome = models.CharField(max_length=100)
    sala = models.ForeignKey(SalaDeAula ,  on_delete=models.DO_NOTHING)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    observacao = models.TextField('Observação', null=True, blank=True)
        
    STATUS_CHOICES = (
        ("QUEBRADO", "Quebrado"),
        ("OK", "Ok"),
        ("EM MANUTENÇÃO", "Em manutenção"),
    )

    status = models.CharField(max_length=20,
        choices=STATUS_CHOICES,  default="AGUARDANDO")

    def get_absolute_url(self):
        return reverse('list_projetores')

    def __str__(self):
        return self.nome