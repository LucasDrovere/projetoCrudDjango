from django.forms import ModelForm, Textarea, TextInput, CharField, ModelChoiceField, Select
from .models import Matricula, Materia, Curso

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['nome', 'cpf', 'ra', 'curso', 'observacoes']
        widgets = {
            'nome' : TextInput(attrs={'placeholder': 'Nome completo do aluno'}),
            'cpf' : TextInput(attrs={'placeholder': 'CPF do aluno', 'type':'number'}),
            'ra' : TextInput(attrs={'placeholder': 'RA do aluno', 'type':'number'}),
            'curso' : Select(attrs={'required': 'required',  'default': '3'}),
            'observacoes': Textarea(attrs={'rows': 4, 'cols': 22, 'style': 'resize:none;', 'placeholder': 'Observações a respeito da matricula'}),
        }