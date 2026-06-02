from django.db import models

class fase_torneo(models.TextChoices):
    GRUPOS = 'Grupos', 'Grupos'
    OCTAVOS = 'Octavos', 'Octavos'
    CUARTOS = 'Cuartos', 'Cuartos'
    SEMIFINAL = 'Semifinal', 'Semifinal'
    FINAL = 'Final', 'Final'

class resultado_tipo(models.TextChoices):
    GANADOR = 'Ganador', 'Ganador'
    PERDEDOR = 'Perdedor', 'Perdedor'
    EMPATE = 'Empate', 'Empate'

# Create your models here.
class encuentro(models.Model):
    id_encuentro = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_torneo = models.IntegerField()
    id_tipo_distribucion = models.IntegerField()
    fase_torneo = models.CharField(
        max_length=20,
        choices=fase_torneo.choices
    )
    id_equipo_1 = models.IntegerField()
    resultado_equipo_1 = models.CharField(
        max_length=20,
        choices=resultado_tipo.choices
    )
    id_equipo_2 = models.IntegerField()
    resultado_equipo_2 = models.CharField(
        max_length=20,
        choices=resultado_tipo.choices
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Encuentro {self.id_encuentro} - Torneo {self.id_torneo} - Fase {self.fase_torneo}"
    
    class Meta:
        db_table = 'encuentro'

class grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    grupo = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Grupo {self.nombre}"
    
    class Meta:
        db_table = 'grupo'


class grupo_encuentro(models.Model):
    id_grupo_encuentro = models.AutoField(primary_key=True)
    id_grupo = models.ForeignKey(
        grupo,
        on_delete=models.CASCADE,
        db_column='id_grupo'
    )
    id_encuentro = models.ForeignKey(
        encuentro,
        on_delete=models.CASCADE,
        db_column='id_encuentro'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Grupo Encuentro {self.id_grupo_encuentro} - Grupo {self.id_grupo} - Encuentro {self.id_encuentro}"
    
    class Meta:
        db_table = 'grupo_encuentro'

class grupo_equipo(models.Model):
    id_grupo_equipo = models.AutoField(primary_key=True)
    id_grupo = models.ForeignKey(
        grupo,
        on_delete=models.CASCADE,
        db_column='id_grupo'
    )
    id_equipo = models.IntegerField()
    partidos_jugados = models.IntegerField(default=0)
    empates = models.IntegerField(default=0)
    victorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Grupo Equipo {self.id_grupo_equipo} - Grupo {self.id_grupo} - Equipo {self.id_equipo}"
    
    class Meta:
        db_table = 'grupo_equipo'
