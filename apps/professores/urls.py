from django.urls import path
from .views import (
                    ProfessoresList,
                    ProfessorEdit,
                    ProfessorDelete,
                    ProfessorNovo
                    )

urlpatterns = [
    path('list/', ProfessoresList.as_view(), name='list_professores'),
    path('editar/<int:pk>/', ProfessorEdit.as_view(), name='update_professor'),
    path('deletar/<int:pk>/', ProfessorDelete.as_view(), name='delete_professor'),
    path('novo/', ProfessorNovo.as_view(), name='create_professor')
]
