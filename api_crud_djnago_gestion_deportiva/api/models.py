from django.db import models

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cantidad_jugadores = models.IntegerField()
    region = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_equipo

    class Meta:
        db_table = 'equipo'

class Premiacion(models.Model):
    id_premiacion = models.AutoField(primary_key=True)
    cantidad_premiacion = models.IntegerField()
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'premiacion'

class Torneo(models.Model):
    id_torneo = models.AutoField(primary_key=True)
    id_tipo_deporte = models.IntegerField()
    nombre_torneo = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.TextField()
    objetivo = models.TextField()
    fecha_fase = models.TextField()
    cantidad_equipo = models.IntegerField()
    id_tipo_distribucion = models.IntegerField()
    id_premiacion = models.ForeignKey(
        Premiacion,
        on_delete=models.CASCADE,
        db_column='id_premiacion'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre_torneo
    
    class Meta:
        db_table = 'torneo'


class Imagen(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    id_torneo = models.ForeignKey(
        Torneo,
        on_delete=models.CASCADE,
        db_column='id_torneo'
    )
    url_imagen = models.TextField()
    tipo_imagen = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url_imagen

    class Meta:
        db_table = 'imagen'


class Distribucion(models.Model):
    id_distribucion = models.AutoField(primary_key=True)
    id_torneo = models.ForeignKey(
        Torneo,
        on_delete=models.CASCADE,
        db_column='id_torneo'
    )
    id_tipo_distribucion = models.IntegerField()
    confirmacion = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.id_tipo_distribucion

    class Meta:
        db_table = 'distribucion'

class Reglamento(models.Model):
    id_reglamento = models.AutoField(primary_key=True)
    id_torneo = models.ForeignKey(
        Torneo,
        on_delete=models.CASCADE,
        db_column='id_torneo'
    )
    id_tipo_reglamento = models.IntegerField()
    id_reglas = models.IntegerField()
    id_tipo_deporte = models.IntegerField()
    idioma = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.id_tipo_reglamento

    class Meta:
        db_table = 'reglamento'


class Integrante(models.Model):
    id_integrante = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE,
        db_column='id_equipo'
    )
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'integrantes'

class Clasificacion(models.Model):
    id_clasificacion = models.AutoField(primary_key=True)
    id_encuentro = models.IntegerField()
    partido_jugado = models.IntegerField()
    partido_ganado = models.IntegerField()
    partido_empatado = models.IntegerField()
    partido_derrota = models.IntegerField()
    puntos_partidos = models.IntegerField()
    id_torneo = models.ForeignKey(
        Torneo,
        on_delete=models.CASCADE,
        db_column='id_torneo'
    )
    id_equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE,
        db_column='id_equipo'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.partido_jugado

    class Meta:
       db_table = 'clasificacion'


class HistorialTorneos(models.Model):
    id_historial = models.AutoField(primary_key=True)
    nombre_torneo = models.CharField(max_length=255)
    id_torneo = models.ForeignKey(
        Torneo,
        on_delete=models.CASCADE,
        db_column='id_torneo'
    )
    id_usuario = models.IntegerField()
    deporte = models.CharField(max_length=100)
    reglamento = models.CharField(max_length=100)
    equipos = models.IntegerField()
    id_tipo_distribucion = models.IntegerField()
    distribucion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    finalizacion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_torneo

    class Meta:
        db_table = 'historialtorneos'        