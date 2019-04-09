from django.urls import path, include
from .views import (
                    Alunolist,
                    Alunolist2,
                    AlunoEdit,
                    AlunoDelete,
                    AlunoNovo,
                    AlunoDetail,
                    )

urlpatterns = [
    path('list_alunos/', Alunolist.as_view(), name='list_alunos'),
    path('list_alunos/nova_matricula/', Alunolist2, name='list_alunos_nova_matricula'),
    path('editar_aluno/<int:pk>', AlunoEdit.as_view(), name='update_aluno'),
    path('deletar_aluno/<int:pk>', AlunoDelete.as_view(), name='deletar_aluno'),
    path('novo_aluno/', AlunoNovo.as_view(), name='novo_aluno'),
    path('aluno_detail/<int:pk>/', AlunoDetail.as_view(), name='detail_aluno')
]
