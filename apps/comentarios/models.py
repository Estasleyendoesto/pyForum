from django.db import models
from ..usuarios.models import Usuario
from ..hilos.models import Post

# Create your models here.
class Comentario(models.Model):
    contenido = models.TextField(max_length=999, blank=False)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.autor.username