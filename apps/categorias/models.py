from django.db import models
from apps.empresas.models import Empresa
from django.urls import reverse

#-------- Categoria Model -------------------------------------

class Categorias(models.Model):

    id =  models.IntegerField(primary_key=True)
    nome = models.CharField('Nome Categoria',max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    datacriacao = models.DateTimeField('Criado em', auto_now_add=True)
    datamodificacao = models.DateTimeField('Modificado em', auto_now=True)


    def get_absolute_url(self):
        return reverse('list_categoria')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome



