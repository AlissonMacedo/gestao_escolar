from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
        ListView,
        UpdateView,
        DeleteView,
        CreateView,
        DetailView
        )
from django.views import View
from .models import Funcionario
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .forms import FuncionarioForm
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioDetail(DetailView):
    model = Funcionario


class FuncionarioEdit(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioNovo(CreateView):
    model = Funcionario
    form_class = FuncionarioForm

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        #username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        username = funcionario.nome +funcionario.segundonome
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        #print(funcionario.aniversario)
        return super(FuncionarioNovo, self).form_valid(form)


def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename"mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(200, 810, "Relatórios de funcionarios - Horas Extras")

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    str_ = 'Nome: %s | Hora Extra: %.2f'

    p.drawString(0, 800, '_' * 150)

    y = 750
    for funcionario in funcionarios:
        p.drawString(20, y, str_ % (funcionario.nome, funcionario.total_horas_extra))
        y -= 40

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    return response

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Redenring PDF", status=400)

class PDF(View):

    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')
