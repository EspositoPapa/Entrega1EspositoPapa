from datetime import datetime
from django.db import models


# Create your models here.
class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    profesion=models.CharField(max_length=40)

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    FechaDeEntrega=models.DateField()
    entregado=models.BooleanField()

class Cursos(models.Model):
    nombre=models.CharField(max_length=30)
    comision=models.IntegerField()

