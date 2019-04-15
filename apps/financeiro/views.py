from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from datetime import date, datetime


from .models import Mensalidades
from django.views.generic import (
                ListView,
                CreateView,
                UpdateView,
                DeleteView,
                DetailView
)

from secretaria.models import Matricula
from .forms import MatriculaFormEditarFinanceiro
from .models import Status_mensalidades, Mensalidades



#----------- Aprovacao de Matriculas -------------------------------

def List_menu_pagamentos_alunos(request):

    matriculas = Matricula.objects.all()

    return render(request, 'financeiro/financeiro_status_pagamentos.html', {'matriculas':matriculas})



#----------- Lista de Mensalidades -------------------------------

def List_mensalidades_status(request, id):

    empresa_logada = request.user.funcionario.empresa

    #Book.objects.filter(authors__nationality='french').filter(authors__sex='f')

    matriculas = Matricula.objects.filter(mensalidades__status_mensalidades=id)


#    mensalidades = Mensalidades.objects.filter(
#        status_mensalidades=id).filter(empresa=empresa_logada).order_by('turma_id')

    return render(request, 'financeiro/list_status_mensalidades.html',
        {'matriculas': matriculas})

#-----------FIM Lista de Mensalidades -------------------------------


def Editar_matriculaaverificar_financeiro(request, id):
    matricula = Matricula.objects.get(id=id)
    form = MatriculaFormEditarFinanceiro(request.POST or None,
            request.FILES or None, instance=matricula)

    if form.is_valid():
        form.save()
        return redirect('list_matriculas_a_verificar_financeiro')

    return render(request, 'vendas/matricula/novo_matricula.html', {'form': form, 'matricula': matricula})


class Detail_matriculasaverificar_financeiro(DetailView):
    model = Matricula



#--------------- Contas a Receber de Alunos -------------------------
#
#---- Toda vez que salvar uma nova matricula a Def chama essa function
#
def defmensalidades(matriculaid, nomeAluno, turma,
        totalapagar, parcelamento, preco, empresa, status_mensalidades):

    a = 0
    parcelaqualdequal = 1


    data_e_hora_atuais = datetime.now()
    #data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
    valordaparcela = preco / parcelamento #precisa considerar desconto
    futuro = data_e_hora_atuais

    while a < parcelamento :

            criar = Mensalidades.objects.create(matriculaid=matriculaid,
                nomeAluno=nomeAluno, turma=turma, totalapagar=totalapagar,
                parcelamento=parcelamento, parcelaqualdequal=parcelaqualdequal,
                valordaparcela=valordaparcela, datadaparcela=futuro,
                empresa=empresa, status_mensalidades=status_mensalidades)

            criar.save()
            a = a + 1
            parcelaqualdequal = parcelaqualdequal + 1

            futuro = date.fromordinal(futuro.toordinal()+30) # hoje + 30 dias
    pass

    return None
