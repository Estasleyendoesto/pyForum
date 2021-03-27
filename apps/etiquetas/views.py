from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Etiqueta, UserTags
from .forms import AddEtiqueta

# Create your views here.
def etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas.html', {'etiquetas':etiquetas})

def user_tag(request, id):
    tag = Etiqueta.objects.get(id=id)
    userTag = UserTags.objects.filter(user=request.user, etiqueta=tag)

    if not userTag:
        userTag = UserTags.objects.create(user=request.user, etiqueta=tag)

    return HttpResponseRedirect(reverse('etiquetas'))

def removeUserTag(request, id):
    tag = UserTags.objects.get(etiqueta=id, user=request.user.id)
    tag.delete()

    return HttpResponseRedirect(reverse('user-tags'))

def buscar_etiqueta(request):
    buscar = request.GET.get('buscar')
    etiquetas = Etiqueta.objects.filter(nombre__icontains=buscar)

    return render(request, 'etiquetas.html', {'etiquetas':etiquetas})

@login_required(login_url='login')
def add_etiqueta(request):
    if request.method == 'POST':
        form = AddEtiqueta(request.POST, request.FILES)
        
        if form.is_valid():
            if form.nada() and form.check_nombre():
                data = form.cleaned_data              
                add = Etiqueta.objects.create(nombre=data['nombre'], adultos=data['adulto'])
                add.imagen = data['imagen']
                add.save()

                return redirect('etiquetas')

    return render(request, 'add-etiqueta.html')

@login_required(login_url='login')
def personalUserTags(request):
    etiquetas = UserTags.objects.filter(user=request.user.id)

    return render(request, 'user-tags.html', {'etiquetas':etiquetas})

@login_required(login_url='login')
def post_tags(request, id):
    etiquetas = Etiqueta.objects.all()
    post = id

    return render(request, 'post-tags.html', {'etiquetas':etiquetas, 'post_id':post})

@login_required(login_url='login')
def add_tags(request):
    data = request.GET.get('data')
    request.session['post-tag'] = data

    return HttpResponse("si")

@login_required(login_url='login')
def changePostTags(request):
    if request.method == "GET":
        data = request.GET.get('data')
        post = request.GET.get('post')
        request.session['post-id'] = post
        request.session['post-tag'] = data

        return HttpResponse("si")