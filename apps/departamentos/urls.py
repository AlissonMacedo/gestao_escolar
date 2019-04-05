from django.urls import path
from .views import (
        DepartamentosList,
        DepartamentoCreate,
        DepartamentoEdit,
        DepartamentoDelete
)

#---- URLs Core -------------------------------------------------------------

urlpatterns = [

    path('list_departamentos/', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamentos'),
    path('editar/<int:pk>/', DepartamentoEdit.as_view(),
            name='update_departamento'),
    path('deletar/<int:pk>/', DepartamentoDelete.as_view(),
            name='delete_departamento'),
]
