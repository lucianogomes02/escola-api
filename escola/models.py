from django.db import models
from enum import Enum


class Nivel(Enum):
    B: str = "Básico"
    I: str = "Intermediário"
    A: str = "Avançado"

    @classmethod
    def opcoes(cls):
        return (
            ("B", cls.B.value),
            ("I", cls.I.value),
            ("A", cls.A.value),
        )


class Periodo(Enum):
    M: str = "Matutino"
    V: str = "Vespertino"
    N: str = "Noturno"

    @classmethod
    def opcoes(cls):
        return (
            ("M", cls.M.value),
            ("V", cls.V.value),
            ("N", cls.N.value),
        )


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(
        max_length=1, choices=Nivel.opcoes(), blank=False, null=False, default="B"
    )

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(
        max_length=1, choices=Periodo.opcoes(), blank=False, null=False, default="M"
    )
