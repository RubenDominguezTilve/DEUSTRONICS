from django.db import models

# Create your models here.


class Usuario(models.Model):
    contrasena = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)


class Empleado(models.Model):
    dni = models.CharField(max_length=9)
