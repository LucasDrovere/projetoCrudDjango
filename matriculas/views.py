from django.shortcuts import render, redirect
import datetime
from .models import Matricula, Materia
from .form import MatriculaForm

def home(request):
    # data = {}
    # data['matriculas'] = ['matricula 1', 'matricula 2', 'matricula 3']
    #
    # data['now'] = datetime.datetime.now()
    # return render(request, 'matriculas/home.html', data)
    return render(request, 'matriculas/home.html')


def listarMatriculados(request):
    data = {}
    data['matriculas'] = Matricula.objects.all()
    return render(request, 'matriculas/listarMatriculados.html', data)


def cadastrarMatricula(request):
    data = {}
    form = MatriculaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_cadastrada')

    data['form'] = form
    return render(request, 'matriculas/cadastrarMatricula.html', data)

def editarMatricula(request, pk):
    data = {}
    matricula = Matricula.objects.get(pk=pk)
    form = MatriculaForm(request.POST or None, instance=matricula)

    if form.is_valid():
        form.save()
        return redirect('url_lista')

    data['form'] = form
    return render(request, 'matriculas/cadastrarMatricula.html', data)

def deletarMatricula(request, pk):
    matricula = Matricula.objects.get(pk=pk)
    matricula.delete()
    return redirect('url_lista')

def matriculaCadastrada(request):
    data = {}
    data['matricula'] = Matricula.objects.last()

    return render(request, 'matriculas/matriculaCadastrada.html', data)