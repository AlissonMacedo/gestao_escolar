from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from apps.core import views
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.registro_hora_extra.api.views import RegistroHoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/horaextra', RegistroHoraExtraViewSet)




#---- URLs Core -------------------------------------------------------------

urlpatterns = [

    path('dashboard/', dashboard, name='dashboard'),
    path('administrativo/', administracao, name='administrativo'),
    path('secretaria/', secretaria, name='secretaria'),
    path('coordenacao/', coordenacao, name='coordenacao'),
    path('logout/', my_logout, name='mylogout'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
