from django.db import models

# modelo de documento 

class Documento(models.Model):
    id_Documento = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo_documento
    class Meta:
        db_table = "documento"


# modelo de usuario

class Usuario (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_documento = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=22)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = "usuario"
    
#  modelo para contraseña
    
class Contrasena (models.Model):
    id_contrasena = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=80)
    hash_contrasena = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.contrasena
    class Meta:
        db_table = "contrasena"

#  modelo para historial_acceso

class HistorialAcceso (models.Model):
    id_historial_acceso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contrasena = models.ForeignKey(Contrasena, on_delete=models.CASCADE)
    fecha_intento = models.DateTimeField()
    exitoso = models.BooleanField(default=True)
    ip_origen = models.CharField(max_length=20)
    fallo_motivo = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.exitoso
    
    class Meta:
        db_table = "historial_acceso"
    
    