from rest_framework import viewsets, generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from escola.models import Aluno, Curso, Matricula
from escola.serializers import (
    AlunoSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculasAlunoSerializer,
    ListaAlunosDoCursoSerializer,
)


class AlunosViewSet(viewsets.ModelViewSet):
    """API de Alunos"""

    queryset = Aluno.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["nome"]
    search_fields = ["nome", "cpf"]
    serializer_class = AlunoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data.get("id"))
            response["Location"] = request.build_absolute_uri() + id
            return response


class CursosViewSet(viewsets.ModelViewSet):
    """API de Cursos"""

    queryset = Curso.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["descricao"]
    serializer_class = CursoSerializer
    http_method_names = ["get", "post", "put", "patch"]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data.get("id"))
            response["Location"] = request.build_absolute_uri() + id
            return response


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


class ListaAlunosDoCurso(generics.ListAPIView):
    """API das Alunos matriculados em um Curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso=self.kwargs.get("pk"))
        return queryset

    serializer_class = ListaAlunosDoCursoSerializer
