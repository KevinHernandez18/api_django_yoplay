from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from .models import Tutoriales

from .serializer import TutorialesSerializer

# crud de tutoriales

class TutorialesViewSet(viewsets.ModelViewSet):
    queryset = Tutoriales.objects.all()
    serializer_class = TutorialesSerializer
    @swagger_auto_schema(
        operation_description="Obtiene la lista de tutoriales"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
