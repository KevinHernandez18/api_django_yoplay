from django.db import models

# modelo de tutoriales

class Tutoriales(models.Model):
    id_tutoriales =models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    link_tuturial = models.CharField(max_length=200)
    fecha_publication = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    class Meta:
        db_table = "tutoriales"