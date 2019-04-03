from django.db import models
from apps.empresas.models import Empresa
from django.urls import reverse

from apps.empresas.models import Empresa
#-------- Aluno Model -------------------------------------


class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    primeironome = models.CharField('Nome', max_length=30)
    segundonome =  models.CharField('Sobrenome', max_length=30)
    idade = models.IntegerField('Idade')
    cpf = models.IntegerField('CPF', null=True, blank=True)
    RG = models.IntegerField('RG', null=True, blank=True)
    datadenascimento = models.DateTimeField('Data Nascimento')
    responsavel = models.CharField('Responsavel', max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_aluno')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['id']

    def __str__(self):
        return self.primeironome + ' ' + self.segundonome



