from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Estado(models.Model):
    nombre = models.CharField(primary_key=True, max_length = 100)

class Estacionamiento(models.Model):
    codigo = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    direccion = models.CharField(max_length = 200)
    latitud = models.CharField(max_length = 30)
    longitud = models.CharField(max_length = 30)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE)
    precio = models.IntegerField()
    img = models.CharField(max_length = 999, default = 'https://i.imgur.com/06j4AsO.png')
    

class Contrato(models.Model):
    codigo = models.AutoField(primary_key = True)
    propietario = models.ForeignKey(User, related_name = 'propietario', on_delete = models.CASCADE)
    arrendador = models.ForeignKey(User, related_name = 'arrendador' ,on_delete = models.CASCADE)
    estacionamiento = models.ForeignKey(Estacionamiento ,on_delete = models.CASCADE)

class Vehiculo(models.Model):
    patente = models.CharField(primary_key = True, max_length = 8)
    marca = models.CharField(max_length = 50)
    color = models.CharField(max_length = 50)
    img = models.CharField(max_length = 999, default = 'https://i.imgur.com/tcsXxV3.png')

class Cuenta(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    estacionamientos = models.ManyToManyField(Estacionamiento, blank = True)
    contratos = models.ManyToManyField(Contrato, blank = True)
    vehiculo = models.ForeignKey(Vehiculo ,on_delete = models.CASCADE)

    numero = models.IntegerField(default=0)
    direccion = models.CharField(max_length = 200, default = "DEFAULT")
    img = models.CharField(max_length = 999, default = 'https://i.imgur.com/a7TW4aZ.png')