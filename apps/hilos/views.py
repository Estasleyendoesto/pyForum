from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from ..usuarios.models import Usuario
from ..general.models import Forum_Stats
from ..comentarios.models import Comentario
from ..comentarios.forms import ComentarioForm
from ..etiquetas.models import PostTags, Etiqueta
from .models import Post
from .forms import CreatePost
import markdown2

# Create your views here.
def post(request, post):
    post = Post.objects.get(id=post)
    html = markdown2.markdown(post.cuerpo, extras=["break-on-newline"])

    if post.visitas:
        post.visitas += 1
    else:
        post.visitas = 1
    post.save()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid() and form.check_comentario():
            comentario = request.POST.get('comentario')
            enviar = Comentario.objects.create(contenido=comentario, autor=request.user, post=post)
            if post.comentarios:
                post.comentarios += 1  
            else:
                post.comentarios = 1      
            post.save()
            forum = Forum_Stats.objects.get(id=1)
            forum.comentarios_totales += 1
            forum.save()
            return HttpResponseRedirect(reverse('post', args=[post.id]))
    else:
        form = ComentarioForm(auto_id=False)

    comentarios = Comentario.objects.filter(post=post.id).order_by('fecha')[:10]

    return render(request, 'post.html', {'post':post, 'form':form, 'comentarios':comentarios, 'next':1, 'html':html})

@login_required(login_url='login')
def creator(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid() and form.check_titulo():
            data = form.cleaned_data
            user = Usuario.objects.get(id=request.user.id)
            post = Post.objects.create(titulo=data['titulo'], cuerpo=data['cuerpo'], autor=user, adultos=data['adultos'], borrador=data['borrador'])
            tag = Etiqueta.objects.get(id=request.session.get('post-tag'))
            postTag = PostTags.objects.create(post=post, etiqueta=tag)
            del request.session['post-tag']
            # Forum +1
            forum = Forum_Stats.objects.get(id=1)
            forum.hilos_creados += 1
            forum.save()

            return redirect('/')
    else:
        form = CreatePost(auto_id=False) 

    return render(request, 'post-editor.html', {'form':form})

@login_required(login_url='login')
def editor(request, post):
    exists = Post.objects.filter(id=post, autor=request.user.id)
    if exists:
        post = Post.objects.get(id=post)
        if request.method == 'POST':
            form = CreatePost(request.POST)
            if form.is_valid() and form.check_titulo():
                data = form.cleaned_data
                post.titulo = data['titulo']
                post.cuerpo = data['cuerpo']
                post.adultos = data['adultos']
                post.borrador = data['borrador']
                post.save()

                post_id = request.session.get('post-id')
                post_tag = request.session.get('post-tag')

                if post_id and post_tag:
                    postTag = PostTags.objects.get(post=post_id)
                    tag = Etiqueta.objects.get(id=post_tag)
                    postTag.etiqueta = tag
                    postTag.save()
                    del request.session['post-id']
                    del request.session['post-tag']

                return HttpResponseRedirect(reverse('post', args=[post.id]))
        else:
            form = CreatePost(auto_id=False)

        return render(request, 'post-editor.html', {'post':post, 'form':form})
    else:
        return redirect('/')