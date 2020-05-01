from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,unique=True)
    def __str__(self):
       return str(f"{self.nombre} {self.apellido1}")


class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
       return self.nombre


class Equipo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoEquipo, on_delete=models.SET_NULL, null=True)
    fecha_adquisicion = models.DateField()
    fecha_instalacion = models.DateField()
    fecha_ultimo_mantenimiento = models.DateField()

    #Revisar
    def __str__(self):
       return str(f"{self.marca}: {self.modelo}")


class Proceso(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
       return self.nombre


class Catalogo(models.Model):
    descripcion = models.CharField(max_length=250)
    nombre = models.CharField(max_length=100, default="NombreDefault")
    precio = models.FloatField(default = 0.0)
    def __str__(self):
       return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,unique=True)
    def __str__(self):
       return self.nombre


class Pedido(models.Model):
    planificado = models.BooleanField()
    producido = models.BooleanField()
    cantidad = models.IntegerField()
    # SET_NULL, null=True por si ya no fabricamos esta pieza, para poder comunicarlo
    catalogo = models.ForeignKey(
        Catalogo, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    importe=models.FloatField()
    #Revisar
    def __str__(self):
       return str(f"REF: {self.cliente.id}.{self.id}")


class Tarea(models.Model):
    finalizada = models.BooleanField(default=False)
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    proceso = models.ForeignKey(Proceso, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    empleados_asignados = models.ManyToManyField(Empleado)
    
    #Revisar
    def __str__(self):
       return str(f"{self.equipo}: {self.proceso} -> de: {self.hora_inicio} a {self.hora_fin}")
