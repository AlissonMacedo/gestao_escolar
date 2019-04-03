from django.urls import path, include
from .views import *

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
    path('novodocumentoaluno/<int:aluno_id>/', DocumentoCreateAluno.as_view(), name='create_documento_aluno'),
    path('novodocumentoprojetor/<int:limpezaprojetor_id>/', DocumentoCreateLimpezaProjetor.as_view(), name='create_documento_limpezaprojetores')
    
]
