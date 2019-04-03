from django.urls import path
from .views import (
        CategoriaList,
        CategoriaCreate,
        CategoriaEdit,
        CategoriaDelete
)

#---- URLs Core -------------------------------------------------------------

urlpatterns = [

    path('list/', CategoriaList.as_view(), name='list_categoria'),
    path('novo/', CategoriaCreate.as_view(), name='create_categoria'),
    path('editar/<int:pk>/', CategoriaEdit.as_view(),
            name='update_categoria'),
    path('deletar/<int:pk>/', CategoriaDelete.as_view(),
            name='delete_categoria'),
]
