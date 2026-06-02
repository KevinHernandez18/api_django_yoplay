
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets


from .models import (
    Reglas,
    Tipo_deporte,
    Tipo_distribucion,
    Tipo_reglamento
)

from .serializer import(
    ReglasSerializer,
    Tipo_deporteSerializer,
    Tipo_distribucionSerializer,
    Tipo_reglamentoSerializer
)

class ReglasViewSet(viewsets.ModelViewSet):
    queryset=Reglas.objects.all()
    serializer_class=ReglasSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class Tipo_deporteViewSet(viewsets.ModelViewSet):
    queryset= Tipo_deporte.objects.all()
    serializer_class=Tipo_deporteSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class Tipo_distribucionViewSet(viewsets.ModelViewSet):
    queryset=Tipo_distribucion.objects.all()
    serializer_class = Tipo_distribucionSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class Tipo_reglamentoViewSet(viewsets.ModelViewSet):
    queryset=Tipo_reglamento.objects.all()
    serializer_class = Tipo_reglamentoSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)