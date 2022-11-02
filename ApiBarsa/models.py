from django.db import models

# Create your models here.

class Barsa(models.Model):
    referencia = models.CharField(max_length=200)
    descripcion = models.TextField()
    nombre_del_club = models.CharField(max_length=200)
    pais_club = models.CharField(max_length=200)
    ciudad_representada = models.CharField(max_length=200)
    edad = models.PositiveIntegerField(default=0)
    titulos = models.CharField(max_length=200)
    nombre_estadio = models.CharField(max_length=200)
    capacidad_estadio = models.PositiveIntegerField(default=0)
    presidente_club = models.CharField(max_length=200)

