from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('coordenacao/listar_matriculas_conferir/',
    list_matriculas_coordenacao_conferir, name='list_matriculas_coordenacao_conferir'),
    path('coordenacao/listar_matriculas_conferidas/',
    list_matriculas_coordenacao_conferidas, name='list_matriculas_coordenacao_conferidas'),
    path('coordenacao/editar_matricula/<int:id>',
    editar_matricula_coordenacao, name='editar_matricula_coordenacao'),

]
