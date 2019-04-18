from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import (
        ListView,
        UpdateView,
        DeleteView,
        CreateView,
        DetailView
        )
from django.views import View
from .models import Aluno
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from .forms import AlunoForm
# ----------------- Funcões para Aluno --- --------------------------



class Alunolist(ListView):
    model = Aluno

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Aluno.objects.filter(empresa=empresa_logada)


def Alunolist2(request):#list aluno para fazer uma nova matricula
    empresa_logada = request.user.funcionario.empresa
    alunos = Aluno.objects.filter(empresa=empresa_logada)
    return render(request, 'aluno/aluno_list2.html', {'alunos':alunos})

class AlunoEdit(UpdateView):
    model = Aluno
    form_class = AlunoForm
    #context_object_name = 'matriculas'

class AlunoDelete(DeleteView):
    model = Aluno
    success_url = reverse_lazy('list_aluno')


class AlunoNovo(CreateView):
    model = Aluno
    form_class = AlunoForm

    def form_valid(self, form):
        aluno = form.save(commit=False)
        aluno.empresa = self.request.user.funcionario.empresa
        #print(aluno.datadenascimento) imprimir datanascimento no console
        aluno.save()

        return super(AlunoNovo, self).form_valid(form)

class AlunoDetail(DetailView):
    model = Aluno
