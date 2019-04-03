from django.urls import path, include
from .views import (
        LimpezaprojetorList,
        LimpezaprojetorDetail,
        LimpezaprojetorEdit,
        LimpezaprojetorNovo,
        LimpezaprojetorDelete
        )

urlpatterns = [
    path('list/', LimpezaprojetorList.as_view(), 
        name='list_projetores'),
    path('detail/<int:pk>/', LimpezaprojetorDetail.as_view(), 
        name='detail_projetores'),
    path('novo/', LimpezaprojetorNovo.as_view(), 
        name='create_projetor'),
    path('editar/<int:pk>/', LimpezaprojetorEdit.as_view(), 
        name='update_projetores'),
    path('deletar/<int:pk>/', LimpezaprojetorDelete.as_view(), 
        name='delete_projetores')
]