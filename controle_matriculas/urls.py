"""controle_matriculas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from matriculas.views import home, listarMatriculados, cadastrarMatricula, editarMatricula, deletarMatricula, \
    exibirCurso, detalharAluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('listarMatriculados/', listarMatriculados, name='url_lista'),
    path('cadastrarMatricula/', cadastrarMatricula, name='url_cadastro'),
    path('editarMatricula/<int:pk>', editarMatricula, name='url_editar'),
    path('deletarMatricula/<int:pk>', deletarMatricula, name='url_deletar'),
    path('exibirCurso/<int:pk>', exibirCurso, name='url_curso'),
    path('detalharAluno/<str:cpf>', detalharAluno, name='url_aluno'),
]
