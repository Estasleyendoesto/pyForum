from django.shortcuts import render
from .models import Forum_Stats
from ..hilos.models import Post
from ..etiquetas.models import Etiqueta, PostTags

# Create your views here.
def home(request):
    forum = Forum_Stats.objects.get(id=1)
    posts = Post.objects.filter(borrador=False).order_by('-creado')[:50]

    return render(request, 'home.html', {'forum':forum, 'posts':posts})

def buscar(request):
    if request.method == 'GET':
        busqueda = request.GET.get('buscar')
        forum = Forum_Stats.objects.get(id=1)
        posts = Post.objects.filter(titulo__icontains=busqueda, borrador=False).order_by('-creado')[:50]

        return render(request, 'home.html', {'forum':forum, 'posts':posts})

    return redirect('/')

def filtrar(request, tag):
    forum = Forum_Stats.objects.get(id=1)
    posts = PostTags.objects.filter(etiqueta=tag)[:50]
    
    return render(request, 'home.html', {'forum':forum, 'posts':posts, 'tag':True})