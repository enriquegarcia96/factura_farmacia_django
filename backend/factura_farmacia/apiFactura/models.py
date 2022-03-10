from django.db import models


# Create your models here.


class Persona(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    GENERO = [(MASCULINO, 'Masculino'), (FEMENINO, 'Femenino')]
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)
    genero = models.CharField(max_length=10, choices=GENERO, null=True)
    numero_identidad = models.CharField(max_length=13)


class Cliente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)



#class Factura(models.Model):
