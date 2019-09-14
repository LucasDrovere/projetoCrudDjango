from django.db import models
from .util import validatorsUtil
from cpffield import cpffield

class Materia(models.Model):
    descricao = models.CharField(max_length=100)
    nome_professor = models.CharField(max_length=100)
    carga_horaria = models.FloatField(max_length=4)

    def __str__(self):
        return self.descricao + ' - ' + self.nome_professor + ' - ' + self.carga_horaria

class Curso(models.Model):
    descricao = models.CharField(max_length=100)
    materias = models.ManyToManyField(Materia)

    def __str__(self):
        return self.descricao

class Matricula(models.Model):
    nome = models.CharField(max_length=100)
    cpf = cpffield.CPFField('CPF', max_length=11, unique=True)
    ra = models.CharField('RA', unique=True, max_length=8)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome + ' - ' + self.ra + ' - ' + self.curso
