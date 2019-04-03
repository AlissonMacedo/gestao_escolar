import datetime
from urllib import request

from django import template

from secretaria.models import Turma, Matricula




register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def turmas_ativas(context):
    empresa = context.request.user.funcionario.empresa
    return len(Turma.objects.filter(status="INICIADA").filter(empresa=empresa))


@register.simple_tag(takes_context=True)
def alunos_ativos(context):
    empresa = context.request.user.funcionario.empresa
    return len(Matricula.objects.filter(status="CURSANDO").filter(empresa=empresa))

@register.simple_tag(takes_context=True)
def alunos_naoativos(context):
    empresa = context.request.user.funcionario.empresa
    return len(Matricula.objects.filter(status="TRANCADA").filter(empresa=empresa))
