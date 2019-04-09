from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.urls import path

#---- URLs Core -------------------------------------------------------------

urlpatterns = [

    path('dashboard/', dashboard, name='dashboard'),
    path('administrativo/', administracao, name='administrativo'),
    path('secretaria/', secretaria, name='secretaria'),
    path('logout/', my_logout, name='mylogout')
]
