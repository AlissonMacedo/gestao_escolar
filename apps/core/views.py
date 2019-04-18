from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from apps.funcionarios.models import Funcionario
from secretaria.models import Turma
from django.views import View
#---- serializers ----
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

#----------- Serialize -----------------------------
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#-------------------------------------------------------

@login_required
def dashboard(request):
    empresa_logada = request.user.funcionario.empresa
    turmas = Turma.objects.filter(status='INICIADA')
    return render(request, 'core/index.html', {'empresa_logada':empresa_logada, 'turmas':turmas})

@login_required
def administracao(request):
    empresa_logada = request.user.funcionario.empresa
    return render(request, 'core/administracao.html', {'empresa_logada':empresa_logada})

@login_required
def secretaria(request):
    empresa_logada = request.user.funcionario.empresa
    return render(request, 'core/secretaria.html', {'empresa_logada':empresa_logada})

@login_required
def coordenacao(request):
    empresa_logada = request.user.funcionario.empresa
    return render(request, 'core/coordenacao.html', {'empresa_logada':empresa_logada})

@login_required
def my_logout(request):
    logout(request)
    return redirect('dashboard')
