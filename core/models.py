from django.db import models

# Create your models here. /libro / autor / categoria /navitem
class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio = models.IntegerField()
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

class Navitem(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre