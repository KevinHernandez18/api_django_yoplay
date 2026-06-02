from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    encuentroViewSet,
    grupoViewSet,
    grupo_encuentroViewSet,
    grupo_equipoViewSet
)

from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="YOPLAY API",
        default_version='v1',
        description="Documentación Swagger de la API de gestión_encuentro",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

# Registro de endpoints del API.

router.register(r'encuentros', encuentroViewSet)
router.register(r'grupos', grupoViewSet)
router.register(r'grupo_encuentros', grupo_encuentroViewSet)
router.register(r'grupo_equipos', grupo_equipoViewSet)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
]
