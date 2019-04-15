from django.conf.urls import url, include
from .views import defmensalidades
from django.urls import path

from .views import (
        List_menu_pagamentos_alunos,
        List_mensalidades_status,
        Editar_matriculaaverificar_financeiro,
        Detail_matriculasaverificar_financeiro
)

#---- URLs Core -------------------------------------------------------------

urlpatterns = [

    path('List_menu_pagamentos/', List_menu_pagamentos_alunos,
        name='list_menu_pagamentos_alunos'),
    path('list_mensalidades/<int:id>/', List_mensalidades_status,
        name='list_mensalidades_status'),
    path('editarmatriculaaverificar/<int:id>', Editar_matriculaaverificar_financeiro,
      name='editar_matriculaaverificar_financeiro'),
    path('detail/<int:pk>/', Detail_matriculasaverificar_financeiro.as_view(),
        name='detail_matriculaaverificar_financeiro'),

]


# SLUG path('list_mensalidades/<slug:opt>'
