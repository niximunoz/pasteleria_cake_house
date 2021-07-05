from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, DateField, IntegerField


# Create your models here.
class Comuna(models.Model):
    
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
dv = [0, "0"],[1, "1"],[2, "2"],[3, "3"],[4, "4"],[5, "5"],[6, "6"],[7, "7"],[8, "8"],[9, "9"],[10, "K"]
class Cliente(models.Model):
    
    rut = models.IntegerField(primary_key=True)
    digito_verificador  = models.IntegerField(choices=dv)
    nombre = CharField(max_length=50)
    apellido_Paterno = models.CharField(max_length=50)
    apellido_Materno = models.CharField(max_length=50)
    email = models.EmailField() 
    fecha_de_Nacimiento = models.DateField()
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(null=True)
    precio_venta = models.IntegerField(null=True)
    descripcion =models.TextField()
    
    def __str__(self):
        return self.nombre