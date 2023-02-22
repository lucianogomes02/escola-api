from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializers import (
    AlunoSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculasAlunoSerializer,
)


class AlunosViewSet(viewsets.ModelViewSet):
    """API de Alunos"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """API de Cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """API de Matriculas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """API das Matriculas do Aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno=self.kwargs.get("pk"))
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer