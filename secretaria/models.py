from datetime import datetime, date, timezone
import datetime
from django.utils import timezone
from django.db import models
from apps.empresas.models import Empresa
from apps.aluno.models import Aluno
from apps.professores.models import Professor
from apps.categoriacursos.models import CategoriaCursos

# -------- Sala de Aula Model -------------------------------------


class SalaDeAula(models.Model):

    nome = models.CharField('Nome ou número da sala', max_length=100)
    qntalunosmax = models.IntegerField(
        'Idade Máxima de alunos', null=True, blank=True)
    observacao = models.TextField('Observação', null=True, blank=True)

    class Meta:
        verbose_name = 'SalaDeAula'
        verbose_name_plural = 'SalaDeAulas'
        ordering = ['nome']

    def __str__(self):
        return self.nome


# -------- Curso Model -------------------------------------

class Curso(models.Model):

    nome = models.CharField('Nome do Curso', max_length=100)
    duracao = models.IntegerField('Duração (Messes)', blank=True)
    qntalunosminimo = models.IntegerField('qnt Alunos Max', blank=True)
    qntalunosmax = models.IntegerField('qnt Alunos Min', blank=True)
    observacao = models.TextField('Observação', blank=True)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    desconto = models.IntegerField('Desconto', blank=True)
    parcelamento = models.IntegerField('Parcelamento', blank=True)
    idademinima = models.IntegerField('Idade Mínima', blank=True)
    idademaxima = models.IntegerField('Idade Máxima', blank=True)
    sala = models.ForeignKey(SalaDeAula,  on_delete=models.DO_NOTHING) #deletar
    materiais = models.TextField('Meteriais', blank=True)
    categoria = models.ForeignKey(
        CategoriaCursos,  on_delete=models.DO_NOTHING, verbose_name='Categorias')
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True)
    datacriacao = models.DateTimeField('Criado em', auto_now_add=True)
    datamodificacao = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-datacriacao']

    def __str__(self):
        return self.nome


# -----------  Turma Model  ---------------------------------------------

class Turma(models.Model):

    turmadocurso = models.ForeignKey(
        Curso, on_delete=models.DO_NOTHING, verbose_name='Curso', related_name='Curso')
    professor = models.ForeignKey(
        Professor,  on_delete=models.DO_NOTHING, verbose_name='Professor', related_name='Professor')
    datainicio = models.DateTimeField('Data Início')
    datafim = models.DateTimeField('Data FIM')
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True)
    sala = models.ForeignKey(SalaDeAula,  on_delete=models.DO_NOTHING)


    DIADASEMANA_CHOICES = (
        (" ---- ", " ---- "),
        ("SEGUNDA", "Segunda"),
        ("TERÇA", "Terça"),
        ("QUARTA", "Quarta"),
        ("QUINTA", "Quinta"),
        ("SEXTA", "Sexta"),
        ("SÁBADO", "Sábado"),
    )

    diadasemana = models.CharField(max_length=9,
                                   choices=DIADASEMANA_CHOICES,
                                   default="----")

    STATUS_CHOICES = (
        ("INICIADA", "Iniciada"),
        ("AGUARDANDO", "Aguardando"),
        ("FINALIZADA", "Finalizada"),
    )

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,  default="AGUARDANDO")

    class Meta:
        verbose_name = 'turmadocurso'
        verbose_name_plural = 'turmadocurso'
        ordering = ['turmadocurso']

    def __str__(self):
        return self.turmadocurso.nome + '  -   Prof  ' + self.professor.primeironome + ' ' + self.professor.segundonome + ' | ' + self.diadasemana + ' | ' + self.status

    def list_matriculas_a_verificar(self):
        return self.turmadocurso.nome + '  -   Prof  ' + self.professor.primeironome + ' | ' + self.diadasemana + ' | ' + self.status

    @property
    def date_diff(self):
        aulas = (self.datafim - self.datainicio).days
        aulas = aulas / 7
        return round(aulas)

    @property
    def date_diff2(self):
        hoje = timezone.now()
        tempocorrido = (hoje - self.datainicio).days
        tempocorrido = tempocorrido / 7
        if tempocorrido < 1:
            tempocorrido = 1
        return round(tempocorrido)

    @property
    def date_diff3(self):
        hoje = timezone.now()
        totaldias = (self.datafim - self.datainicio).days
        tempocorrido = (hoje - self.datainicio).days
        porcentagem = round(( tempocorrido * 100) / totaldias)
        return porcentagem




# ---------Matricula Model -------------------------------------------------------------------


class Matricula(models.Model):
    nomeAluno = models.ForeignKey(
        Aluno, on_delete=models.DO_NOTHING, verbose_name='Aluno', related_name='Aluno')
    turma = models.ForeignKey(
        Turma, on_delete=models.DO_NOTHING, verbose_name='Turma', related_name='Turma')
    preco =models.IntegerField('preco', blank=True)
    totalapagar = models.IntegerField('total a pagar', blank=True)
    desconto = models.IntegerField('Desconto', blank=True)
    parcelamento = models.IntegerField('Parcelamento X Vezes ', blank=True)
    varlorparcelas = models.IntegerField('Valor Parcelas ', blank=True)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True)
    observacao = models.TextField('Observação', null=True, blank=True)
    status_coordenacao = models.BooleanField('Status Coordenaç',default=False)
    status_financeiro = models.BooleanField(default=False)

    #models.DecimalField(
        #'Total a Pagar', decimal_places=2, max_digits=10)

    STATUS_CHOICES = (
        ("CURSANDO", "Cursando"),
        ("AGUARDANDO", "Aguardando"),
        ("TRANCADA", "Trancada"),
    )

    status = models.CharField('Status', max_length=10,
                              choices=STATUS_CHOICES,  default="AGUARDANDO")

    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
        ordering = ['nomeAluno']

    def __str__(self):
        return self.nomeAluno.primeironome


# ----------------------------------------------------


class Brand(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return {'name': self.name, 'brand': self.brand.company_name}
