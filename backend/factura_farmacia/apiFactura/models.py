from django.db import models
from django.forms import model_to_dict


# Create your models here.


class Persona(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    GENERO = [(MASCULINO, 'Masculino'), (FEMENINO, 'Femenino')]
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)
    genero = models.CharField(
        max_length=10, choices=GENERO, default='Masculino')
    numero_identidad = models.CharField(max_length=13)


class Factura(models.Model):
    fecha = models.DateField
    total = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    numeroIdentidad = models.ForeignKey(Persona, on_delete=models.CASCADE)


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)


class Producto(models.Model):
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=6, decimal_places=2)
    nombre_producto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    fecha_elaboracion = models.DateField
    fecha_vencimiento = models.DateField
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True)


# todo: hacer factura de detalle con la relacion que tienen
