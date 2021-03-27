from django.db import models

# Create your models here.
class Forum_Stats(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    usuarios_registrados = models.IntegerField(null=True)
    hilos_creados = models.IntegerField(null=True)
    comentarios_totales = models.IntegerField(null=True)
    usuarios_online = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre
