# from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DocumentoViewSet,
    UsuarioViewSet,
    ContrasenaViewSet,
    HistorialAccesoViewSet
)
# from django.contrib import admin
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

router = DefaultRouter()

# registro de los endpoints del api

router.register(r'documento', DocumentoViewSet, basename='documento')
router.register(r"usuario",UsuarioViewSet, basename='usuario')
router.register(r'contrasena',ContrasenaViewSet, basename='contrasena')
router.register(r'historial_acceso',HistorialAccesoViewSet, basename='historial_acceso')


urlpatterns = router.urls