from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializers import AlunoSerializer, CursoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """API de Alunos"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """API de Cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
