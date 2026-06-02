
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets



from .models import (
    Equipo,
    Premiacion,
    Torneo,
    Imagen,
    Distribucion,
    Reglamento,
    Integrante,
    Clasificacion,
    HistorialTorneos,
)

from .serializers import (
    EquipoSerializer,
    PremiacionSerializer,
    TorneoSerializer,
    ImagenSerializer,
    DistribucionSerializer,
    ReglamentoSerializer,
    IntegranteSerializer,
    ClasificacionSerializer,
    HistorialTorneosSerializer,
)


# crud de tutoriales





# CRUD tabla equipo
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# CRUD tabla premiacion
class PremiacionViewSet(viewsets.ModelViewSet):
    queryset = Premiacion.objects.all()
    serializer_class = PremiacionSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# CRUD tabla torneo
class TorneoViewSet(viewsets.ModelViewSet):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# CRUD tabla imagen
class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# CRUD tabla distribucion
class DistribucionViewSet(viewsets.ModelViewSet):
    queryset = Distribucion.objects.all()
    serializer_class = DistribucionSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# CRUD tabla reglamento
class ReglamentoViewSet(viewsets.ModelViewSet):
    queryset = Reglamento.objects.all()
    serializer_class = ReglamentoSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# CRUD tabla integrantes
class IntegranteViewSet(viewsets.ModelViewSet):
    queryset = Integrante.objects.all()
    serializer_class = IntegranteSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# CRUD tabla clasificacion
class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# CRUD tabla historial torneos
class HistorialTorneosViewSet(viewsets.ModelViewSet):
    queryset = HistorialTorneos.objects.all()
    serializer_class = HistorialTorneosSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

