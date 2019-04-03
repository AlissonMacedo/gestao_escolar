from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('vendas/listar_curso/', list_curso, name='list_curso'),
    path('vendas/novo_curso/', novo_curso, name='novo_curso'),
    path('vendas/editar_curso/<int:id>', editar_curso, name='editar_curso'),
    path('vendas/deletar_curso/<int:id>', deletar_curso, name='deletar_curso'),

    path('vendas/listar_sala/', list_sala, name='list_sala'),
    path('vendas/novo_sala/', novo_sala, name='novo_sala'),
    path('vendas/editar_sala/<int:id>', editar_sala, name='editar_sala'),
    path('vendas/deletar_sala/<int:id>', deletar_sala, name='deletar_sala'),

#---- URLs de Matriculas -----------------------------------------------

     path('vendas/listar_matricula/', list_matricula, name='list_matricula'),
     path('vendas/novo_matricula/<int:idaluno>/<int:idturma>', novo_matricula, name='novo_matricula'),
     path('vendas/editar_matricula/<int:id>', editar_matricula, name='editar_matricula'),
 #   path('vendas/deletar_professor/<int:id>', deletar_professor, name='deletar_professor'),

#---- URLs Turmas -----------------------------------------------

     path('vendas/listar_turma/', list_turma, name='list_turma'),
     path('vendas/listar_turma2/<int:idaluno>', list_turma2, name='list_turma2'),
     path('vendas/novo_turma/', novo_turma, name='novo_turma'),
     path('vendas/editar_turma/<int:id>', editar_turma, name='editar_turma'),
     path('vendas/deletar_turma/<int:id>', deletar_turma, name='deletar_turma'),
     path('vendas/detail/<int:pk>/', ListTurmasDetail.as_view(), 
        name='detail_turma'),
    path('vendas/matriculadosturma/<int:id>/', MatriculadosTurmaList, 
        name='matriculadosturma'),


#---- URLs teste submenu -----------------------------------------------


    path('vendas/saregcar', regcar, name='regcar'),


]
