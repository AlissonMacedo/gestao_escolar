from django.db import models
from django.urls import reverse
from apps.aluno.models import Aluno
from secretaria.models import Matricula, Turma
from apps.empresas.models import Empresa
import datetime

class Status_mensalidades(models.Model):
    status = models.CharField(max_length=18)


    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('dashboard')


class Mensalidades(models.Model):
    matriculaid = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING)
    nomeAluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    totalapagar = models.IntegerField('Total a pagar', null=True, blank=True)
    parcelamento = models.IntegerField('Parcelamento', null=True, blank=True)
    parcelaqualdequal = models.IntegerField('Parcela qual de qual', null=True, blank=True)
    datadaparcela = models.DateField(default=datetime.date.today, null=True, blank=True)
    valordaparcela = models.IntegerField('Valor da parcela', null=True, blank=True)
    status_mensalidades = models.ForeignKey(Status_mensalidades, null=False, blank=False, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.matriculaid + ' ' + self.nomeAluno

    def get_absolute_url(self):
        return reverse('dashboard')
