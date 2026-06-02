from django.urls import path, include
from rest_framework.routers import DefaultRouter


# from django.urls import path, include 


# from django.contrib import admin
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

from .views import (
    EquipoViewSet,
    PremiacionViewSet,
    TorneoViewSet,
    ImagenViewSet,
    DistribucionViewSet,
    ReglamentoViewSet,
    IntegranteViewSet,
    ClasificacionViewSet,
    HistorialTorneosViewSet
)

router = DefaultRouter()

# Registro endpoints
router.register(r'equipos', EquipoViewSet, basename='equipos')
router.register(r'premiaciones', PremiacionViewSet, basename='premiaciones')
router.register(r'torneos', TorneoViewSet, basename='torneos')
router.register(r'imagenes', ImagenViewSet, basename='imagenes')
router.register(r'distribuciones', DistribucionViewSet, basename='distribucion')
router.register(r'reglamentos', ReglamentoViewSet, basename='reglamento')
router.register(r'integrantes', IntegranteViewSet, basename='integrantes')
router.register(r'clasificaciones', ClasificacionViewSet, basename='clasificaciones')
router.register(r'historialtorneos', HistorialTorneosViewSet,basename='historialtorneos')

urlpatterns = router.urls