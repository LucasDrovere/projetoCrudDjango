from django.forms import ModelForm, Textarea, TextInput, CharField, ModelChoiceField, Select
from .models import Matricula, Materia, Curso, Aluno

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['nome', 'cpf', 'ra', 'curso', 'observacoes']
        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Nome completo do aluno'}),
            'cpf': TextInput(attrs={'placeholder': 'CPF do aluno', 'data-mask':"000.000.000-00"}),
            'ra': TextInput(attrs={'placeholder': 'RA do aluno', 'data-mask':"00000-000"}),
            'curso': Select(attrs={'required': 'required',  'default': '3'}),
            'observacoes': Textarea(attrs={'rows': 4, 'cols': 22, 'style': 'resize:none;', 'placeholder': 'Observações a respeito da matricula'}),
        }

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'dt_nascimento', 'cpf', 'rg', 'cep', 'curso', 'bolsista', 'observacoes']
        widgets = {
            'nome': TextInput(attrs={'readonly':'readonly'}),
            'curso': TextInput(attrs={'readonly':'readonly'}),
            'cpf': TextInput(attrs={'readonly':'readonly'}),
        }