from rest_framework import serializers
from .models import (
    Documento, 
    Usuario, 
    Contrasena, 
    HistorialAcceso
)

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields= '__all__'
        
class ContrasenaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Contrasena
        fields = '__all__'
        
class HistorialAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialAcceso
        fields = '__all__'