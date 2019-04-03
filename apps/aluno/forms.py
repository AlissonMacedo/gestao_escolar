from django import forms
from .models import *

#-------- Aluno Form -------------------------------------


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['primeironome','segundonome', 
            'idade','cpf','RG','datadenascimento', 
            'responsavel','id']

