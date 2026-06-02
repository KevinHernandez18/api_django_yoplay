from django.urls import path, include
from rest_framework.routers import DefaultRouter



from .views import (
    ReglasViewSet,
    Tipo_deporteViewSet,
    Tipo_distribucionViewSet,
    Tipo_reglamentoViewSet
)

router = DefaultRouter()

router.register(r'Reglas',ReglasViewSet, basename='Reglas')
router.register(r'Tipo_deporte',Tipo_deporteViewSet, basename='Tipo_deporte')
router.register(r'Tipo_distribucion',Tipo_distribucionViewSet , basename='Tipo_distribucion')
router.register(r'Tipo_reglamento',Tipo_reglamentoViewSet, basename='Tipo_reglamento')

urlpatterns =router.urls
