from django.db import models

# Create your models here.

class Usuario(models.Model):
    contrasena = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)


class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Equipo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()
    fecha_instalacion = models.DateField()
    fecha_ultimo_mantenimiento = models.DateField()


class Tarea(models.Model):
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL)
    proceso = models.ForeignKey(Proceso, on_delete=models.SET_NULL)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL)


class Proceso(models.Model):
    nombre = models.CharField(max_length=100)


class AsignacionTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)


class Catalogo(models, Model):
    descripcion = models.CharField(max_length=250)


class Pedido(models.Model):
    planifiado = models.BooleanField()
    producido = models.BooleanField()
    cantidad = models.IntegerField()
    # set_null por si ya no fabricamos esta pieza, para poder comunicarlo
    catalogo = models.ForeignKey(Catalogo, on_delete=models.SET_NULL)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
