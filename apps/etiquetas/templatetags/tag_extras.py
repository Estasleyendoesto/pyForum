from django import template
from ..models import UserTags, Etiqueta, PostTags
from django.utils.text import Truncator

register = template.Library()

@register.simple_tag
def exists(tag, user):
    userTag = UserTags.objects.filter(user=user, etiqueta=tag)

    if userTag:
        return True
    else:
        return False

@register.simple_tag
def postExists(tag, post):
    postTag = PostTags.objects.filter(post=post, etiqueta=tag)

    if postTag:
        return True
    else:
        return False

@register.simple_tag
def lista(user):
    tags = UserTags.objects.filter(user=user)[:7]
    response = ''
    for tag in tags:
        nombre = Truncator(tag.etiqueta.nombre).chars(21)
        response += '<li><a href="/tag-post/'+ str(tag.etiqueta.id) +'/" data-title="'+ tag.etiqueta.nombre +'"><img src="'+ str(tag.etiqueta.imagen.url) +'">'+ nombre +'</a></li>'
        #response += '<li><a href="/buscar-etiqueta/?buscar='+ tag.etiqueta.nombre +'" data-title="'+ tag.etiqueta.nombre +'"><img src="'+ str(tag.etiqueta.imagen.url) +'">'+ nombre +'</a></li>'

    return response

@register.simple_tag
def listaOff():
    tags = Etiqueta.objects.all().order_by('?')[:7]
    response = ''
    for tag in tags:
        nombre = Truncator(tag.nombre).chars(21)
        response += '<li><a href="/tag-post/'+ str(tag.id) +'/" data-title="'+ tag.nombre +'"><img src="'+ str(tag.imagen.url) +'">'+ nombre +'</a></li>'
        #response += '<li><a href="/buscar-etiqueta/?buscar='+ tag.nombre +'" data-title="'+ tag.nombre +'"><img src="'+ str(tag.imagen.url) +'">'+ nombre +'</a></li>'

    return response

@register.simple_tag
def load_tags(post):
    tag = PostTags.objects.get(post=post)

    return '<a href="/buscar-etiqueta/?buscar='+ tag.etiqueta.nombre +'">'+ tag.etiqueta.nombre +'</a>'

@register.simple_tag
def find_tag(post):
    tag = PostTags.objects.get(post=post)

    return '<a href="/tag-post/'+ str(tag.etiqueta.id) +'/">'+ tag.etiqueta.nombre +'</a>'

@register.simple_tag
def load_img(post):
    tag = PostTags.objects.get(post=post)

    return '<img class="image-tag" src="'+ tag.etiqueta.imagen.url +'" width="30" height="30" style="border-radius: 50%; margin-right: 5px;">'

@register.simple_tag
def load_img_post(post):
    tag = PostTags.objects.get(post=post)

    return '<img class="image-tag" src="'+ tag.etiqueta.imagen.url +'" width="40" height="40" style="border-radius: 50%; margin-right: 1px;">'