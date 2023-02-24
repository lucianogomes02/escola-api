from django.contrib import admin
from django.urls import path, include
from escola.views import (
    AlunosViewSet,
    CursosViewSet,
    MatriculasViewSet,
    ListaMatriculasAluno,
    ListaAlunosDoCurso,
)
from rest_framework import routers, permissions
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Escola-API",
        default_version="v1",
        description="API de Registro de Alunos, Cursos e Matrículas dos Alunos nos Cursos",
        terms_of_service="#",
        contact=openapi.Contact(email="lucianogvda02@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matriculas", MatriculasViewSet, basename="Matriculas")


urlpatterns = [
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("controle-api/", admin.site.urls),
    path("", include(router.urls)),
    path("alunos/<int:pk>/matriculas", ListaMatriculasAluno.as_view()),
    path("cursos/<int:pk>/matriculas", ListaAlunosDoCurso.as_view()),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
