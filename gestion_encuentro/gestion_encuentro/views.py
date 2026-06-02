from django.shortcuts import render

from rest_framework import viewsets

from .models import(
    encuentro, 
    grupo, 
    grupo_encuentro, 
    grupo_equipo
)

from .serializers import(
    encuentroSerializer,
    grupoSerializer,
    grupo_encuentroSerializer,
    grupo_equipoSerializer
)

class encuentroViewSet(viewsets.ModelViewSet):
    queryset = encuentro.objects.all()
    serializer_class = encuentroSerializer

class grupoViewSet(viewsets.ModelViewSet):
    queryset = grupo.objects.all()
    serializer_class = grupoSerializer

class grupo_encuentroViewSet(viewsets.ModelViewSet):
    queryset = grupo_encuentro.objects.all()
    serializer_class = grupo_encuentroSerializer

class grupo_equipoViewSet(viewsets.ModelViewSet):
    queryset = grupo_equipo.objects.all()
    serializer_class = grupo_equipoSerializer