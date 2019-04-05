from django.urls import path, include
from .views import (
        FuncionariosList,
        FuncionarioEdit,
        FuncionarioDelete,
        FuncionarioNovo,
        PDF
        )
from .views import relatorio_funcionarios

urlpatterns = [
    path('list_funcionarios', FuncionariosList.as_view(), 
        name='list_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(),
        name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(),
        name='update_funcionarios'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(),
        name='delete_funcionario'),
    path('pdf-reportlab/', relatorio_funcionarios,
        name='pdf-reportlab'),
    path('relatorio_funcionarios_html/', PDF.as_view(),
        name='relatorio_funcionarios_html'),

]
