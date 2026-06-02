from rest_framework import serializers

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


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'


class PremiacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premiacion
        fields = '__all__'


class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = '__all__'


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'


class DistribucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribucion
        fields = '__all__'


class ReglamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reglamento
        fields = '__all__'


class IntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrante
        fields = '__all__'


class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = '__all__'


class HistorialTorneosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialTorneos
        fields = '__all__'