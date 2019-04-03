from django.conf.urls import url, include
from .views import EmpresaCreate, EmpresaEdit
from django.urls import path

#---- URLs Core -------------------------------------------------------------

urlpatterns = [

    path('novo', EmpresaCreate.as_view(), name='crete_empresa'),
    path('editar/<int:pk>/',
        EmpresaEdit.as_view(), name='edit_empresa'),


]
