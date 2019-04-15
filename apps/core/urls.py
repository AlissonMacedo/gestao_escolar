from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from apps.core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)




#---- URLs Core -------------------------------------------------------------

urlpatterns = [

    path('dashboard/', dashboard, name='dashboard'),
    path('administrativo/', administracao, name='administrativo'),
    path('secretaria/', secretaria, name='secretaria'),
    path('logout/', my_logout, name='mylogout'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
