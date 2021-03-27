from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Comentario

# Create your views here.
def mas_comentarios(request):
    if request.is_ajax():
        post = request.GET.get('post')
        page = request.GET.get('next')

        ini = int(page) * 10
        comentarios = Comentario.objects.filter(post=post).order_by('fecha')[ini : ini + 10]
        total = Comentario.objects.filter(post=post).count()

        response = render_to_string('comentarios.html', {'comentarios':comentarios, 'next':int(page) + 1, 'total':total})
        return HttpResponse(response)