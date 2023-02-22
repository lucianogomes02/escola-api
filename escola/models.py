from django.db import models
from enum import Enum


class Nivel(Enum):
    B: str = "Básico"
    I: str = "Intermediário"
    A: str = "Avançado"

    @classmethod
    def opcoes(cls):
        return (
            ("B", cls.B),
            ("I", cls.I),
            ("A", cls.A),
        )


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
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
