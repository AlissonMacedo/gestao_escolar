from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
        ListView,
        UpdateView,
        DeleteView,
        CreateView
        )

from .models import Professor


class ProfessoresList(ListView):
    model = Professor

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Professor.objects.filter(empresa=empresa_logada)


class ProfessorEdit(UpdateView):
    model = Professor
    fields = ['primeironome', 'segundonome', 'idade',
    'cpf', 'RG', 'datadenascimento', 'cursoApto', 'foto', 'observacao']


class ProfessorDelete(DeleteView):
    model = Professor
    success_url = reverse_lazy('list_professores')


class ProfessorNovo(CreateView):
    model = Professor
    fields = ['primeironome', 'segundonome', 'idade',
    'cpf', 'RG', 'datadenascimento', 'cursoApto', 'foto', 'observacao']

    def form_valid(self, form):
        professor = form.save(commit=False)
        professor.empresa = self.request.user.funcionario.empresa
        professor.save()
        return super(ProfessorNovo, self).form_valid(form)

