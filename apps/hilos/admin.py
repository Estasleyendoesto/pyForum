from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor', 'titulo', 'visitas', 'comentarios', 'adultos', 'borrador', 'creado', 'modificado')

admin.site.register(Post, PostAdmin)