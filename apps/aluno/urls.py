from django.urls import path, include
from .views import (
                    Alunolist,
                    AlunoEdit,
                    AlunoDelete,
                    AlunoNovo,
                    AlunoDetail,
                    )

urlpatterns = [
    path('', Alunolist.as_view(), name='list_aluno'),
    path('editar_aluno/<int:pk>', AlunoEdit.as_view(), name='update_aluno'),
    path('deletar_aluno/<int:pk>', AlunoDelete.as_view(), name='deletar_aluno'),
    path('novo_aluno/', AlunoNovo.as_view(), name='novo_aluno'),
    path('aluno_detail/<int:pk>/', AlunoDetail.as_view(), name='detail_aluno')
]