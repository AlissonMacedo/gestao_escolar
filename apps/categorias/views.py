from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
                ListView,
                CreateView,
                UpdateView,
                DeleteView
)
from .models import  Categorias

class CategoriaList(ListView):
    model = Categorias

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Categorias.objects.filter(empresa=empresa_logada)


class CategoriaCreate(CreateView):
    model = Categorias
    fields = ['nome']


    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(CategoriaCreate, self).form_valid(form)


class CategoriaEdit(UpdateView):
    model = Categorias
    fields = ['nome']


class CategoriaDelete(DeleteView):
    model = Categorias
    success_url = reverse_lazy('list_categorias')
