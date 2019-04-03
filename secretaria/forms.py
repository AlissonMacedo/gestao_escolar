from django import forms
from .models import *


#-------- Curso Form -------------------------------------


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome','duracao', 'qntalunosminimo',
        'qntalunosmax', 'observacao', 'preco', 'desconto',
        'parcelamento', 'idademinima', 'idademaxima', 'sala',
        'materiais', 'categoria']
#-------- Salas de Aula Form -------------------------------------

class SalaForm(forms.ModelForm):
    class Meta:
        model = SalaDeAula
        fields = ['nome','qntalunosmax','observacao']


#------------------------------------------------------------------


class MatriculaForm(forms.ModelForm):
   class Meta:
       model = Matricula
       fields = ['preco','desconto', 'parcelamento', 'totalapagar', 'observacao']


class MatriculaFormEditar(forms.ModelForm):
   class Meta:
       model = Matricula
       fields = ['status','preco','desconto', 'parcelamento', 'totalapagar', 'observacao']


#---------------------------------------------------------------------


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['turmadocurso', 'professor', 'datainicio', 'datafim', 'diadasemana',
        'status']
        datainicio = forms.DateField(input_formats=["%d/%m/%Y",], widget=forms.DateInput(format='%d/%m/%Y')
)