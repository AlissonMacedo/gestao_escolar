from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.urls import reverse
from django.db.models import Sum

class Funcionario(models.Model):
    nome = models.CharField(max_length=18)
    segundonome = models.CharField(max_length=18)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(max_length=70,blank=True)
    imagem = models.ImageField(upload_to = 'foto-funcionario/')
    aniversario = models.DateField(null=True)
    regiao = models.CharField(max_length=18)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    @property
    def total_horas_extra(self):
        total = self.registrohoraextra_set.filter(ultilizada=False).aggregate(Sum('horas')) ['horas__sum']
        return total or 0

    def __str__(self):
        return self.nome + " " + self.segundonome
