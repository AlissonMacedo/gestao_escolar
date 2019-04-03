from django.urls import path
from .views import (
                    CategoriaCursosCreate,
                    CategoriaCursosList,
                    CategoriaCursosEdit,
                    CategoriaCursosDelete
                    )

#---- URLs Core -------------------------------------------------------------

urlpatterns = [

    path('list/', CategoriaCursosList.as_view(), 
                    name='list_categoriacursos'),
    path('novo/', CategoriaCursosCreate.as_view(), 
                    name='create_categoriacursos'),
    path('editar/<int:pk>/', CategoriaCursosEdit.as_view(),
                    name='update_categoriacursos'),
    path('deletar/<int:pk>/', CategoriaCursosDelete.as_view(),
                    name='delete_categoriacursos'),
]
