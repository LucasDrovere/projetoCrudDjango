from django.contrib import admin
from .models import Matricula
from .models import Materia
from .models import Curso

admin.site.register(Matricula)
admin.site.register(Materia)
admin.site.register(Curso)
