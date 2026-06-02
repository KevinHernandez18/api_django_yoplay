from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from .models import Documento, Usuario, Contrasena, HistorialAcceso

from .serializers import DocumentoSerializer, UsuarioSerializer, ContrasenaSerializer, HistorialAccesoSerializer

# crud de documento 

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de documento"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
# crud de usuario
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
# crud de contrasena
    
class ContrasenaViewSet(viewsets.ModelViewSet):
    queryset = Contrasena.objects.all()
    serializer_class = ContrasenaSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de contrasena"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
# crud de historial_acceso
    
class HistorialAccesoViewSet(viewsets.ModelViewSet):
    queryset = HistorialAcceso.objects.all()
    serializer_class = HistorialAccesoSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de historial_acceso"
        )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)