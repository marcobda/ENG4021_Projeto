from django.db import models

class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    professor = models.CharField(max_length=120,help_text='Nome do professor avaliado')
    materia = models.CharField(max_length=120,help_text='Nome da matéria avaliada')
    universidade = models.CharField(max_length=120,help_text='Nome da universidade')
    nota = models.DecimalField(max_digits=3,decimal_places=1,help_text='Nota geral do professor (0 a 10)')
    comentario = models.TextField(help_text='Comentário do aluno (opcional)',blank=True,null=True)
    data_avaliacao = models.DateField(help_text='Data da avaliação',auto_now_add=True)
    anonimo = models.BooleanField(default=True,help_text='O aluno quer ficar anônimo?')

    def __str__(self):
        return f"{self.professor} - {self.materia} ({self.nota})"
