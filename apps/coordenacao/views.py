import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from secretaria.models import Matricula

from .forms import MatriculaCoordenacaoFormEditar

from django.http import HttpResponse


# ---------- Funções para COODENACAO Conferir e Conferidas ------------------------------------------

@login_required
def list_matriculas_coordenacao_conferir(request):
    matriculas = Matricula.objects.filter(status_coordenacao=False)
    return render(request, 'coordenacao/list_matricula_conferir.html', {'matriculas': matriculas})

@login_required
def list_matriculas_coordenacao_conferidas(request):
    matriculas = Matricula.objects.filter(status_coordenacao=True)
    return render(request, 'coordenacao/list_matricula_conferidas.html', {'matriculas': matriculas})

def editar_matricula_coordenacao(request, id):
    matricula = Matricula.objects.get(id=id)
    empresa_logada = request.user.funcionario.empresa
    aluno = matricula.nomeAluno
    turma = matricula.turma


    form = MatriculaCoordenacaoFormEditar(request.POST or None,
                               request.FILES or None, instance=matricula)

    if form.is_valid():
        form.save()
        return redirect('coordenacao')

    return render(request, 'coordenacao/editar_matricula.html', {'form': form, 'matricula': matricula})

# ---------- FIM para COODENACAO ------------------------------------------
