from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Forum_Stats

# Register your models here.
admin.site.site_header = 'Administración'
admin.site.site_title = 'Administración'

class Forum_stats_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'usuarios_registrados', 'hilos_creados', 'comentarios_totales', 'usuarios_online')

admin.site.register(Forum_Stats, Forum_stats_admin)
admin.site.unregister(Group)