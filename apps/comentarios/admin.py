from django.contrib import admin
from .models import Comentario

# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'contenido', 'autor', 'post')

admin.site.register(Comentario, ComentarioAdmin)