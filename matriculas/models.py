from django.db import models
from .util.validatorsUtil import validate_CPF
from cpffield import cpffield

class Materia(models.Model):
    descricao = models.CharField(max_length=100)
    nome_professor = models.CharField(max_length=100)
    carga_horaria = models.FloatField(max_length=4)

    def __str__(self):
        return self.descricao + ' - ' + self.nome_professor

class Curso(models.Model):
    descricao = models.CharField(max_length=100)
    materias = models.ManyToManyField(Materia)

    def __str__(self):
        return self.descricao

class Matricula(models.Model):
    nome = models.CharField(max_length=100)
    cpf = cpffield.CPFField('CPF', max_length=14, unique=True)
    ra = models.CharField('RA', unique=True, max_length=9)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=None)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField('Observações', null=True, blank=True)

    def __str__(self):
        return self.nome + ' - ' + self.ra

class Aluno(models.Model):
    nome = models.CharField(null=True, blank=True, max_length=100)
    dt_nascimento = models.DateTimeField('Data de nascimento', null=True, blank=True)
    cpf = cpffield.CPFField('CPF', null=True, blank=True, max_length=14)
    rg = models.CharField('RG', unique=True, max_length=12, null=True, blank=True)
    cep = models.CharField('CEP',  max_length=9, null=True, blank=True)
    curso = models.CharField(null=True, blank=True, max_length=100)
    bolsista = models.BooleanField(default=False, blank=True)
    observacoes = models.TextField('Observações', null=True, blank=True)

