from django.db import models
from django.shortcuts import reverse

from apps.funcionarios.models import Funcionario
from apps.aluno.models import Aluno
from apps.tecnologiadainformacao.models import projetor


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertense = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_funcionarios', 
            args=[self.pertense.id])

    def __str__(self):
        return self.descricao


class DocumentoAluno(models.Model):
    descricao = models.CharField(max_length=100)
    pertense = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentosAlunos')

    def get_absolute_url(self):
        return reverse('update_aluno', 
            args=[self.pertense.id])

    def __str__(self):
        return self.descricao


class DocumentoProjetor(models.Model):
    descricao = models.CharField(max_length=100)
    pertense = models.ForeignKey(projetor, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentosProjetor')

    def get_absolute_url(self):
        return reverse('update_projetores', 
            args=[self.pertense.id])

    def __str__(self):
        return self.descricao
