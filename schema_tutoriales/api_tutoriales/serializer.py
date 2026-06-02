from rest_framework import serializers
from .models import Tutoriales
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class TutorialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutoriales
        fields = '__all__'

# token JWT
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def valiate(self, data):
        user =authenticate(    
            username = data.get('username'),
            password = data.get('password')
        )
        if user is not None:
            return user
        raise serializers.ValidationError('usuario o contraseña incorrectos')