from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = (
            ('Datos personales', {'fields': ('frase', 'image',)}),
            *UserAdmin.fieldsets,
        )
    list_display = ('id', 'username', 'email', 'is_active', 'last_login', 'date_joined')

admin.site.register(Usuario, UsuarioAdmin)