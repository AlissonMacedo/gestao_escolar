from django import forms
from .models import *

#-------- Aluno Form -------------------------------------


class AlunoForm(forms.ModelForm):
    datadenascimento = forms.DateField(input_formats=["%d/%m/%Y",], widget=forms.DateInput(format='%d/%m/%Y')),
    
    class Meta:
        model = Aluno
        fields = ['primeironome','segundonome',
            'idade','cpf','RG','datadenascimento',
            'responsavel','id']
