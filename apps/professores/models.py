from django.db import models
from apps.empresas.models import Empresa
from django.urls import reverse

class Professor(models.Model):
    primeironome = models.CharField('Nome', max_length=30)
    segundonome = models.CharField('Sobrenome', max_length=30)
    idade = models.IntegerField('Idade', null=True, blank=True)
    cpf = models.IntegerField('CPF', null=True, blank=True)
    RG = models.IntegerField('RG', null=True, blank=True)
    datadenascimento = models.DateTimeField('Data Nascimento', null=True, blank=True)
    cursoApto = models.CharField('curso Apto', max_length=60, null=True, blank=True)
    foto = models.ImageField(upload_to='professor_photo', null=True, blank=True)
    observacao = models.TextField('Observação', null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_professores')

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['primeironome']

    def __str__(self):
        return self.primeironome + ' ' + self.segundonome

