from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from apps.core import views

# Gabiarra para funcionar os arquivos staticos --------------

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


#--------   + static (settings.MEDIA_URL, document_roo=settings.MEDIA_ROOT)

#---- URLs Principal -------------------------------------------------------------


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('apps.core.urls')),
    url(r'^', include('apps.home.urls')),
    path('tecnologiadainformacao/', include('apps.tecnologiadainformacao.urls')),
    path('categoria/', include('apps.categoriacursos.urls')),
    path('financeiro/', include('apps.financeiro.urls')),
    path('professores/', include('apps.professores.urls')),
    path('alunos/', include('apps.aluno.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('documentosAlunos/', include('apps.documentosAlunos.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    url(r'^', include('secretaria.urls')),

    path('login/', auth_views.LoginView.as_view(), name='login'), # Importa view de login do Django

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
