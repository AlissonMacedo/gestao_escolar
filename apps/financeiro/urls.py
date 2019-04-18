from django.conf.urls import url, include
from .views import defmensalidades
from django.urls import path

from .views import *


#---- URLs Core -------------------------------------------------------------

urlpatterns = [
    path('financeiro/listar_matriculas_conferir/',
    list_matriculas_financeiro_conferir, name='list_matriculas_financeiro_conferir'),
    path('financeiro/listar_matriculas_conferidas/',
    list_matriculas_financeiro_conferidas, name='list_matriculas_financeiro_conferidas'),
    path('financeiro/editar_matricula/<int:id>',
    editar_matricula_financeiro, name='editar_matricula_financeiro'),

#-------------------------------------------------------------------------------------------

    path('aluno_list_financeiro/', aluno_list_financeiro,
        name='aluno_list_financeiro'),
    path('list_menu_pagamentos_alunos/', List_menu_pagamentos_alunos,
        name='list_menu_pagamentos_alunos'),
    path('list_mensalidades/<int:id>/', List_mensalidades_status,
        name='list_mensalidades_status'),
    path('editarmatriculaaverificar/<int:id>', Editar_matriculaaverificar_financeiro,
      name='editar_matriculaaverificar_financeiro'),
    path('detail/<int:pk>/', Detail_matriculasaverificar_financeiro.as_view(),
        name='detail_matriculaaverificar_financeiro'),

]


# SLUG path('list_mensalidades/<slug:opt>'
