from django.urls import reverse_lazy
from django.views.generic import (
        ListView,
        DetailView,
        UpdateView,
        DeleteView,
        CreateView
        )

from apps.tecnologiadainformacao.models import projetor

class LimpezaprojetorList(ListView):
    model = projetor

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return projetor.objects.filter(empresa=empresa_logada)


class LimpezaprojetorDetail(DetailView):
    model = projetor

class LimpezaprojetorEdit(UpdateView):
    model = projetor
    fields = ['numerodeserie', 'sala', 'nome', 'status', 'observacao']


class LimpezaprojetorDelete(DeleteView):
    model = projetor
    success_url = reverse_lazy('list_projetores')


class LimpezaprojetorNovo(CreateView):
    model = projetor
    fields = ['numerodeserie', 'sala', 'nome','status', 'observacao']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.save()
        return super(LimpezaprojetorNovo, self).form_valid(form)

