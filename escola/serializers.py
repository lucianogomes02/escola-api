from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"

    @staticmethod
    def validate_nome(nome):
        if not all([palavra.isalpha() for palavra in nome.split(" ")]):
            raise serializers.ValidationError(
                "O nome não deve conter caractéres numéricos."
            )
        return nome

    @staticmethod
    def validate_rg(rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 dígitos.")
        return rg

    @staticmethod
    def validate_cpf(cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 dígitos.")
        return cpf


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]

    def get_periodo(self, objeto):
        return objeto.get_periodo_display()


class ListaAlunosDoCursoSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source="aluno.nome")

    class Meta:
        model = Matricula
        fields = ["aluno"]
