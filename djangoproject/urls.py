"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.general import views as general
from apps.usuarios import views as usuario
from apps.hilos import views as hilo
from apps.comentarios import views as comentarios
from apps.etiquetas import views as etiquetas

# Borrar tras finalizar desarrollo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', general.home, name='home'),
    path('search/', general.buscar, name='buscar'),
    path('login/', usuario.login, name='login'),
    path('logout/', usuario.logout, name='logout'),
    path('registro/', usuario.registro, name='registro'),
    path('profile/<str:user>/', usuario.profile, name='profile'),
    path('settings/', usuario.profileConfig, name='profile-settings'),
    path('settings-persona/', usuario.personalForm, name='personal-form'),
    path('settings-prefer/', usuario.preferForm, name='prefer-form'),
    path('settings-account/', usuario.accountForm, name='account-form'),
    path('creator/', hilo.creator, name='post-creator'),
    path('editor/<int:post>/', hilo.editor, name='post-editor'),
    path('hilo/<int:post>', hilo.post, name='post'),
    path('comentarios/', comentarios.mas_comentarios, name='comentarios'),
    path('etiquetas/', etiquetas.etiquetas, name='etiquetas'),
    path('user-tag/<int:id>/', etiquetas.user_tag, name='user-tag'),
    path('remove-tag/<int:id>/', etiquetas.removeUserTag, name='remove-tag'),
    path('buscar-etiqueta/', etiquetas.buscar_etiqueta, name='buscar-etiqueta'),
    path('add-etiqueta/', etiquetas.add_etiqueta, name='add-etiqueta'),
    path('user-tags/', etiquetas.personalUserTags, name='user-tags'),
    path('post-tags/<int:id>/', etiquetas.post_tags, name='post-tags'),
    path('add-tags/', etiquetas.add_tags, name='add-tags'),
    path('change-post-tags/', etiquetas.changePostTags, name='change-post-tags'),
    path('tag-post/<int:tag>/', general.filtrar, name='filtrar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  # Borrar +... tras finalizar desarrollo