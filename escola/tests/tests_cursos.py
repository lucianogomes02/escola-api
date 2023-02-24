from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Cursos-list")
        self.user = User.objects.create_superuser(
            email="test@gmail.com",
            password="1234567",
            username="usuario teste",
        )
        self.client.force_authenticate(self.user)
        self.primeiro_curso = Curso.objects.create(
            codigo_curso="CTT1", descricao="Curso Teste 1", nivel="B"
        )
        self.segundo_curso = Curso.objects.create(
            codigo_curso="CTT2", descricao="Curso Teste 2", nivel="I"
        )

    def test_get_cursos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_curso(self):
        data = {"codigo_curso": "CTT3", "descricao": "Curso Teste 3", "nivel": "A"}

        response = self.client.post(self.list_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_curso(self):
        response = self.client.delete("/cursos/1/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_curso(self):
        data = {"codigo_curso": "CTT1", "descricao": "Curso Teste 1 Att", "nivel": "I"}
        response = self.client.put("/cursos/1/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
