from rest_framework.test import APITestCase
from escola.models import Aluno
from escola.serializers import AlunoSerializer
from validate_docbr import CPF
from datetime import date


class AlunoSerializerTestCase(APITestCase):
    def setUp(self):
        self.aluno = Aluno(
            nome="Aluno Serializado",
            cpf=CPF().generate(),
            rg="123456789",
            data_nascimento=date(2000, 1, 1),
            foto="",
        )
        self.serializer = AlunoSerializer(instance=self.aluno)

    def test_valida_campos_serializados(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set(["id", "nome", "cpf", "rg", "data_nascimento", "foto"]),
        )

    def test_valida_valores_dos_campos_serializados(self):
        data = self.serializer.data
        self.assertEqual(data.get("id"), self.aluno.id)
        self.assertEqual(data.get("nome"), self.aluno.nome)
        self.assertEqual(data.get("cpf"), self.aluno.cpf)
        self.assertEqual(data.get("rg"), self.aluno.rg)
        self.assertEqual(
            data.get("data_nascimento"), self.aluno.data_nascimento.strftime("%Y-%m-%d")
        )
        self.assertEqual(data.get("foto"), None)
