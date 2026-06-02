from rest_framework import serializers

from .models import (
    encuentro,
    grupo,
    grupo_encuentro,
    grupo_equipo
)

class encuentroSerializer(serializers.ModelSerializer):
    class Meta:
        model = encuentro
        fields = '__all__'

class grupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = grupo
        fields = '__all__'

class grupo_encuentroSerializer(serializers.ModelSerializer):
    class Meta:
        model = grupo_encuentro
        fields = '__all__'

class grupo_equipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = grupo_equipo
        fields = '__all__'
