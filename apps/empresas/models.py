from django.db import models
from django.urls import reverse

class Empresa(models.Model):
    nome = models.CharField(max_length=13, help_text='Nome fantasia')
    razao_social = models.CharField(max_length=80)
#    cliente_classificacao = models.ForeignKey(ClienteClassificacao, null=False, blank=False, on_delete=models.PROTECT)
#    cliente_situacao = models.ForeignKey(ClienteSituacao, null=False, blank=False, on_delete=models.PROTECT)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=100)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('dashboard')
