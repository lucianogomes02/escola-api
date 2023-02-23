from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from escola.validators import cpf_valido, nome_valido, rg_valido


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"

    @staticmethod
    def validate(data):
        if not nome_valido(data.get("nome", "")):
            raise serializers.ValidationError(
                {"nome": "O nome não deve conter caractéres numéricos."}
            )
        elif not rg_valido(data.get("rg", "")):
            raise serializers.ValidationError(
                {
                    "rg": "O RG deve ter 9 dígitos e deve conter apenas carácteres númericos."
                }
            )
        elif not cpf_valido(data.get("cpf", "")):
            raise serializers.ValidationError({"cpf": "Número de CPF inválido."})
        return data


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
