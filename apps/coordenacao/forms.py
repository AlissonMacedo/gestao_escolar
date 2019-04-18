from django import forms
from secretaria.models import Matricula


#-------- Coordenacao Form -------------------------------------

class MatriculaCoordenacaoFormEditar(forms.ModelForm):
   class Meta:
       model = Matricula
       fields = ['status', 'status_coordenacao', 'observacao']


#--------FIM  Coordenacao Form -------------------------------------
