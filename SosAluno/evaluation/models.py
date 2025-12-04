from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Faculdade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Faculdade"
        verbose_name_plural = "Faculdades"

    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Matéria"
        verbose_name_plural = "Matérias"

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=150)
    faculdade = models.ForeignKey(Faculdade, on_delete=models.CASCADE)
    materias = models.ManyToManyField(Materia)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        unique_together = ('nome', 'faculdade')

    def __str__(self):
        return f"{self.nome} ({self.faculdade.nome})"

class Avaliacao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Nota de 1 a 5 estrelas"
    )
    comentario = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        unique_together = ('professor', 'aluno') 

    def __str__(self):
        return f"Avaliação de {self.professor.nome} por {self.aluno.username} - Nota: {self.nota}"