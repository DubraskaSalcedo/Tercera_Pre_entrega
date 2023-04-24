from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Taller(models.Model):
    title = models.CharField(max_length=100, unique=True)
    intro = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    fecha = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="avatares_cursos", null="True", blank="True", default=None)
    def __str__(self):
        return str(self.title) + ', ' + str(self.author)
class Comentario(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, default=None)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha) + ', ' + str(self.cuerpo)