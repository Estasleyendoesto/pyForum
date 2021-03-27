from django.db import models
from ..usuarios.models import Usuario
from ..hilos.models import Post

# Create your models here.
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='tags/', default='tags/default.jpg')
    adultos = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class UserTags(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)

class PostTags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)