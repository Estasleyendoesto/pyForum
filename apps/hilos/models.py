from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=70)
    cuerpo = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentarios = models.IntegerField(null=True)
    visitas = models.IntegerField(null=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    borrador = models.BooleanField(default=False)
    adultos = models.BooleanField(default=False)

    def __str__(self):
        return '@%s: %s' % (self.autor.username, self.titulo)