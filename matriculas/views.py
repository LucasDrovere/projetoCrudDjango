from django.shortcuts import render, redirect
import datetime
from .models import Matricula, Materia, Curso, Aluno
from .form import MatriculaForm, AlunoForm
from pprint import pprint

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
        return redirect('url_lista')

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

def exibirCurso(request, pk):
    data = {}
    matricula = Matricula.objects.get(pk=pk)
    materiasCurso = matricula.curso.materias.all()

    data['matricula'] = matricula
    data['materiasCurso'] = materiasCurso

    data['nomeCurso'] = matricula.curso.descricao.upper()

    return render(request, 'cursos/exibirCurso.html', data)

def detalharAluno(request, cpf):
    data = {}
    matricula = Matricula.objects.get(cpf=cpf)

    aluno = Aluno()

    try:
        aluno = Aluno.objects.get(cpf=cpf)
    except Aluno.DoesNotExist:
        aluno.nome = matricula.nome
        aluno.cpf = matricula.cpf
        aluno.curso = matricula.curso.descricao

    form = AlunoForm(request.POST or None, instance=aluno)

    if request.method == 'POST':
        form.save()

    data['form'] = form
    data['matricula'] = matricula

    return render(request, 'alunos/detalharAluno.html', data)