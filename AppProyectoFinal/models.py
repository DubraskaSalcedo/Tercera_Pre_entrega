from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

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
class Curso3(models.Model):
    title = models.CharField(max_length=100, unique=True)
    intro = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    fecha = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title + ', ' + str(self.author.first_name) + ' ' + str(self.author.last_name)

class Comentario(models.Model):
    curso3 = models.ForeignKey(Curso3, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=20, default=None)

    def __str__(self):
        return str(self.fecha) + ', ' + str(self.cuerpo)