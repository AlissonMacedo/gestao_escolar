from django import forms
from secretaria.models import Matricula


class MatriculaFormEditarFinanceiro(forms.ModelForm):
   class Meta:
       model = Matricula
       fields = ['preco','desconto', 'parcelamento',
        'totalapagar', 'observacao']
        # 'statusfinanceiro',
        #'emitidosBoletos']
