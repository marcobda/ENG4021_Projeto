from django.contrib import admin
from .models import Professor, Universidade, Disciplina, Avaliacao

admin.site.register(Professor)
admin.site.register(Universidade)
admin.site.register(Disciplina)
admin.site.register(Avaliacao)
