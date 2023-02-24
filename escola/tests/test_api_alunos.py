from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from datetime import datetime
from validate_docbr import CPF


class AlunosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Alunos-list")
        self.user = User.objects.create_superuser(
            email="test@gmail.com",
            password="1234567",
            username="usuario teste",
        )
        self.client.force_authenticate(self.user)
        self.primeiro_aluno = Aluno.objects.create(
            cpf=CPF().generate(),
            nome="Aluno Teste Um",
            rg="000000000",
            data_nascimento=datetime(2000, 1, 1),
            foto="",
        )
        self.segundo_aluno = Aluno.objects.create(
            cpf=CPF().generate(),
            nome="Aluno Teste Dois",
            rg="111111111",
            data_nascimento=datetime(2000, 2, 1),
            foto="",
        )

    def test_get_alunos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_aluno(self):
        data = {
            "nome": "Aluno Teste Três",
            "cpf": CPF().generate(),
            "rg": "222222222",
            "data_nascimento": "2000-03-01",
            "foto": "",
        }

        response = self.client.post(self.list_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_aluno(self):
        data = {
            "nome": "Aluno Teste Um Att",
            "cpf": self.primeiro_aluno.cpf,
            "rg": "000000000",
            "data_nascimento": "2000-01-01",
            "foto": "",
        }
        response = self.client.put("/alunos/1/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_aluno(self):
        response = self.client.delete("/alunos/2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
