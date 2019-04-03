from django.shortcuts import render
from django.views.generic import CreateView
from .models import (
                    Documento,
                    DocumentoProjetor,
                    DocumentoAluno
                    )

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertense_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DocumentoCreateAluno(CreateView):
    model = DocumentoAluno
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertense_id = self.kwargs['aluno_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class DocumentoCreateLimpezaProjetor(CreateView):
    model = DocumentoProjetor
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertense_id = self.kwargs['limpezaprojetor_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)