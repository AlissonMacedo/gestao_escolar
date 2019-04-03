from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
                ListView,
                CreateView,
                UpdateView,
                DeleteView
)
from .models import  CategoriaCursos

class CategoriaCursosList(ListView):
    model = CategoriaCursos

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return CategoriaCursos.objects.filter(empresa=empresa_logada)


class CategoriaCursosCreate(CreateView):
    model = CategoriaCursos
    fields = ['nome']


    def form_valid(self, form):
        categoria = form.save(commit=False)
        categoria.empresa = self.request.user.funcionario.empresa
        categoria.save()
        return super(CategoriaCursosCreate, self).form_valid(form)


class CategoriaCursosEdit(UpdateView):
    model = CategoriaCursos
    fields = ['nome']


class CategoriaCursosDelete(DeleteView):
    model = CategoriaCursos
    success_url = reverse_lazy('list_categoriacursos')
