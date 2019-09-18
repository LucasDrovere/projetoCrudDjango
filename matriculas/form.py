from django.forms import ModelForm, Textarea, TextInput, CharField, ModelChoiceField, Select, DateTimeField, CheckboxInput
from .models import Matricula, Materia, Curso, Aluno
from bootstrap_datepicker_plus import DatePickerInput


class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['nome', 'cpf', 'ra', 'curso', 'observacoes']
        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Nome completo do aluno'}),
            'cpf': TextInput(attrs={'placeholder': 'CPF do aluno', 'data-mask': "000.000.000-00"}),
            'ra': TextInput(attrs={'placeholder': 'RA do aluno', 'data-mask': "00000-000"}),
            'curso': Select(attrs={'required': 'required', 'default': '3'}),
            'observacoes': Textarea(attrs={'rows': 4, 'cols': 22, 'style': 'resize:none;',
                                           'placeholder': 'Observações a respeito da matricula'}),
        }


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['foto', 'nome', 'dt_nascimento', 'cpf', 'rg', 'cep', 'curso', 'bolsista', 'observacoes']
        widgets = {
            'nome': TextInput(attrs={'readonly': 'readonly'}),
            'dt_nascimento': DatePickerInput(options={
                "format": "DD/MM/YYYY",
                "locale": "pt",
            },
                attrs={'placeholder': 'Ex: 31/12/2000', 'data-mask': "00/00/0000"}
            ),
            'curso': TextInput(attrs={'readonly': 'readonly'}),
            'cpf': TextInput(attrs={'readonly': 'readonly'}),
            'rg': TextInput(attrs={'placeholder': 'RG do aluno', 'data-mask': "00.000.000-0"}),
            'cep': TextInput(attrs={'placeholder': 'CEP do endereço do aluno', 'data-mask': "00000-000"}),
            'observacoes': Textarea(attrs={'rows': 5, 'cols': 22, 'style': 'resize:none;',
                                           'placeholder': 'Observações a do aluno'}),
            'bolsista': CheckboxInput(attrs={
                'style':'width:20px;height:20px;', 'id': 'checkbolsista'})
        }
