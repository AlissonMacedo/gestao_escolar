from django.urls import path, include
from .views import (
        FuncionariosList,
        FuncionarioEdit,
        FuncionarioDelete,
        FuncionarioNovo,
        FuncionarioDetail,
        PDF
        )
from .views import relatorio_funcionarios

urlpatterns = [
    path('list_funcionarios', FuncionariosList.as_view(),
        name='list_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(),
        name='novo_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(),
        name='editar_funcionario'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(),
        name='deletar_funcionario'),
    path('detalhes/<int:pk>/', FuncionarioDetail.as_view(),
        name='detalhes_funcionario'),
    path('pdf-reportlab/', relatorio_funcionarios,
        name='pdf-reportlab'),
    path('relatorio_funcionarios_html/', PDF.as_view(),
        name='relatorio_funcionarios_html'),

]
