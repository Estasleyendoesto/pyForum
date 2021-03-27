from django.contrib import admin
from .models import Etiqueta, UserTags, PostTags

# Register your models here.
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'adultos', 'creado')

class UserTagsAdmin(admin.ModelAdmin):
    list_display = ('user', 'etiqueta')

admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(UserTags, UserTagsAdmin)
admin.site.register(PostTags)