from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    grupo = models.IntegerField(unique=True)
    activado = models.BooleanField(default=False)

    def __str__(self):
        return f"Curso: {self.nombre} Grupo: {self.grupo}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}"