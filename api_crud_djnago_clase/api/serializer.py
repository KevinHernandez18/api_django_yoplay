from rest_framework import serializers

from .models import (
    Reglas,
    Tipo_deporte,
    Tipo_distribucion,
    Tipo_reglamento
)

class ReglasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reglas
        fields = '__all__'

class Tipo_deporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_deporte
        fields = '__all__'

class Tipo_distribucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_distribucion 
        fields = '__all__'

class Tipo_reglamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_reglamento
        fields = '__all__'