from django.forms import ModelForm
from .models import Matricula, Materia

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['nome', 'cpf', 'ra', 'curso', 'observacoes']