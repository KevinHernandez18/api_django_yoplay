from django.db import models

# Modelo tabla Jugador
class Reglas(models.Model):
    id_reglas = models.AutoField(primary_key=True)
    cantidad_reglas = models.IntegerField()
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return str(self.id_reglas)
        
    class Meta:
            db_table = 'reglas'


# Modelo tabla videojuego
class Tipo_deporte(models.Model):
    id_tipo_deporte = models.AutoField(primary_key=True)
    nombre_deporte  = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_deporte

    class Meta:
        db_table = 'tipo_deporte'


# Modelo tabla partida
class Tipo_distribucion(models.Model):
    id_tipo_distribucion = models.AutoField(primary_key=True)
    equipo = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.equipo

    class Meta:
        db_table = 'tipo_distribucion'


class Tipo_reglamento(models.Model):
    id_tipo_reglamento = models.AutoField(primary_key=True)
    id_tipo_deporte =models.ForeignKey(
    Tipo_deporte,
     on_delete=models.CASCADE, 
     db_column='id_tipo_deporte')
    nombre_tipo = models.CharField(max_length=30)
    descripcion = models.TextField()

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tipo_reglamento{self.id_tipo_reglamento}"
    class Meta:
        db_table = 'tipo_reglamento'