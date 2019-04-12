from django import forms
from .models import *


#-------- Curso Form -------------------------------------


class FuncionarioForm(forms.ModelForm):
    aniversario = forms.DateField(input_formats=["%d/%m/%Y",], widget=forms.DateInput(format='%d/%m/%Y')),
    telefone = forms.CharField(widget=forms.TextInput(attrs={'data-mask':"000-00000-0000"}))
    class Meta:
        model = Funcionario
        fields = ['nome', 'segundonome', 'telefone', 'email', 'aniversario', 'imagem', 'regiao', 'departamento']
