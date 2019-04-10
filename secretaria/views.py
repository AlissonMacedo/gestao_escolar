import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Curso,
    Aluno,
    SalaDeAula,
    Matricula,
    Turma
)

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView
)

from .forms import CursoForm, SalaForm, MatriculaForm, MatriculaFormEditar, TurmaForm
from .models import Brand, Car
from apps.departamentos.models import Departamento
from django.core import serializers
from django.http import HttpResponse


# ----------------------- Funcões para Cursos ----------------------------------

@login_required
def list_curso(request):
    cursos = Curso.objects.all()
    return render(request, 'vendas/curso/list_curso.html', {'cursos': cursos})


@login_required
def novo_curso(request):
    form = CursoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_curso')

    return render(request, 'vendas/curso/novo_curso.html', {'form': form})


@login_required
def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    form = CursoForm(request.POST or None, instance=curso)

    if form.is_valid():
        form.save()
        return redirect('list_curso')

    return render(request, 'vendas/curso/novo_curso.html', {'form': form, 'curso': curso})


@login_required
def deletar_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == 'POST':
        curso.delete()
        return redirect('list_curso')

    return render(request, 'vendas/curso/confirm_deletar_curso.html', {'curso': curso})

# -------- Funcões para Salas  -------------------------------------------


@login_required
def list_sala(request):
    salas = SalaDeAula.objects.all()
    return render(request, 'vendas/sala/list_sala.html', {'salas': salas})


@login_required
def novo_sala(request):
    form = SalaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_sala')

    return render(request, 'vendas/sala/novo_sala.html', {'form': form})


@login_required
def editar_sala(request, id):
    sala = SalaDeAula.objects.get(id=id)
    form = SalaForm(request.POST or None,
                    request.FILES or None, instance=sala)

    if form.is_valid():
        form.save()
        return redirect('list_sala')

    return render(request, 'vendas/sala/novo_sala.html', {'form': form, 'sala': sala})


@login_required
def deletar_sala(request, id):
    sala = SalaDeAula.objects.get(id=id)

    if request.method == 'POST':
        sala.delete()
        return redirect('list_sala')

    return render(request, 'vendas/sala/confirm_deletar_sala.html', {'sala': sala})


# -------- Funcões para Turma  -------------------------------------------

@login_required
def list_turma(request):
    turmas = Turma.objects.all()
    return render(request, 'vendas/turma/list_turma.html', {'turmas': turmas})


def list_turma2(request, idaluno):
    turmas = Turma.objects.all()
    aluno = Aluno.objects.get(id=idaluno)
    return render(request, 'vendas/turma/list_turma2.html', {'turmas': turmas, 'aluno': aluno})


@login_required
def novo_turma(request):
    form = TurmaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        turma = form.save(commit=False)
        turma.empresa = request.user.funcionario.empresa
        turma.save()
        return redirect('list_turma')

    return render(request, 'vendas/turma/novo_turma.html', {'form': form})


@login_required
def editar_turma(request, id):
    turma = Turma.objects.get(id=id)
    form = TurmaForm(request.POST or None,
                     request.FILES or None, instance=turma)

    if form.is_valid():
        form.save()
        return redirect('list_turma')

    return render(request, 'vendas/turma/novo_turma.html', {'form': form, 'turma': turma})


@login_required
def deletar_turma(request, id):
    turma = Turma.objects.get(id=id)

    if request.method == 'POST':
        turma.delete()
        return redirect('list_turma')

    return render(request, 'vendas/turma/confirm_deletar_turma.html', {'turma': turma})


# ---------- Funções para matricula ------------------------------------------

@login_required
def list_matriculas(request):
    matriculas = Matricula.objects.all()
    return render(request, 'vendas/matricula/list_matricula.html', {'matriculas': matriculas})


def novo_matricula(request, idaluno, idturma):
    aluno = Aluno.objects.get(id=idaluno)
    turma = Turma.objects.get(id=idturma)
    form = MatriculaForm(request.POST or None, request.FILES or None)
    parcelas = turma.turmadocurso.parcelamento
    preco = turma.turmadocurso.preco
    desconto = turma.turmadocurso.desconto

    if form.is_valid():
        novamatricula = form.save(commit=False)
        novamatricula.nomeAluno = aluno
        novamatricula.turma = turma
        novamatricula.preco = preco
        novamatricula.totalapagar = preco - desconto
        novamatricula.desconto = desconto
        novamatricula.varlorparcelas = novamatricula.totalapagar / novamatricula.parcelamento
        novamatricula.empresa = request.user.funcionario.empresa
        novamatricula.save()

        return redirect('list_matriculas')

    return render(request, 'vendas/matricula/novo_matricula.html',
        {'form': form, 'aluno': aluno, 'turma': turma, 'range':range(0,parcelas), 'parcelas':parcelas})


@login_required
def editar_matricula(request, id):
    matricula = Matricula.objects.get(id=id)
    empresa_logada = request.user.funcionario.empresa
    aluno = matricula.nomeAluno
    turma = matricula.turma

    departamentos = Departamento.objects.all()

    form = MatriculaFormEditar(request.POST or None,
                               request.FILES or None, instance=matricula)

    if form.is_valid():
        form.save()
        return redirect('list_matriculas')

    return render(request, 'vendas/matricula/novo_matricula.html', {'form': form, 'matricula': matricula, 'aluno':aluno, 'turma':turma})

def deletar_matricula(request, id):
    matricula = Matricula.objects.get(id=id)

    if request.method == 'POST':
        turma.delete()
        return redirect('list_matriculas')

    return render(request, 'vendas/listar_matriculas/list_matricula.html', {'matricula': matricula})

# ---------- Funções para matricula ------------------------------------------

@login_required
def deletar_turma(request, id):
    turma = Turma.objects.get(id=id)

    if request.method == 'POST':
        turma.delete()
        return redirect('list_turma')

    return render(request, 'vendas/turma/confirm_deletar_turma.html', {'turma': turma})


class ListTurmasDetail(DetailView):
    model = Turma

def MatriculadosTurmaList(request, id):
    matriculas = Matricula.objects.filter(turma=id)

    return render(request, 'vendas/turma/matriculados_turma.html', {'matriculas':matriculas})

def filtra_funcionarios(request):
    depart = request.GET['outro_param']
    departamento = Departamento.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.funcionario_set.all())
    return HttpResponse(qs_json, content_type='application/json')

# -------------------------------------------------------------------------


def regcar(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    dcars = {}
    for car in cars:
        brand = str(car.brand)
        if brand in dcars:
            dcars[brand].append(car.name)
        else:
            dcars[brand] = [car.name]
    cars = json.dumps(dcars)
    brands = json.dumps([str(b) for b in brands])
    return render(request, 'vendas/regcar.html', {'brands': brands, 'cars': cars})
