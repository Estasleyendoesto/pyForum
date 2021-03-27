from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .forms import RegistroUsuario, LoginUsuario, PersonalForm, PreferForm, AccountEmailForm, AccountPasswordForm
from ..general.models import Forum_Stats
from ..hilos.models import Post
from .models import Usuario

# Create your views here.
def profile(request, user):
    usuario = Usuario.objects.get(username=user)
    if request.user.is_authenticated:
        if request.user.id == usuario.id:
            posts = Post.objects.filter(autor=usuario.id).order_by('-creado')[:50]
        else:
            posts = Post.objects.filter(autor=usuario.id, borrador=False).order_by('-creado')[:50]
    else:
        posts = Post.objects.filter(autor=usuario.id, borrador=False).order_by('-creado')[:50]

    return render(request, 'profile.html', {'usuario':usuario, 'posts':posts})

def registro(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = RegistroUsuario(request.POST)

            if form.is_valid() and form.nada() and form.check_username() and form.check_email() and form.check_password():
                data = form.cleaned_data
                user = Usuario.objects.create_user(data['username'], data['email'], data['pass_1'])   
                forum = Forum_Stats.objects.get(id=1)
                forum.usuarios_registrados += 1
                forum.save()
                return redirect('home')
        else:
            form = RegistroUsuario(auto_id=False)

        return render(request, 'registro.html', {'form':form})
    return redirect('home')
    
def login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = LoginUsuario(request.POST)

            if form.is_valid() and form.nada():
                user = form.check_user(request)

                if user:
                    data = form.cleaned_data
                    do_login(request, user)

                    forum = Forum_Stats.objects.get(id=1)
                    if forum.usuarios_online:
                        forum.usuarios_online += 1
                    else:
                        forum.usuarios_online = 1
                    forum.save()

                    return redirect('home')
        else:
            form = LoginUsuario(auto_id=False)
        
        return render(request, 'login.html', {'form':form})
    return redirect('home')

def logout(request):
    do_logout(request)
    forum = Forum_Stats.objects.get(id=1)
    forum.usuarios_online -= 1
    forum.save()

    return redirect('home')

@login_required(login_url='login')
def profileConfig(request):
    return render(request, 'profile_config.html')
        
@login_required(login_url='login')
def personalForm(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST, request.FILES)
        if form.is_valid():
            user = Usuario.objects.get(id=request.user.id)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.frase = form.cleaned_data['frase']

            if form.cleaned_data['imagen']:
                user.image = form.cleaned_data['imagen']

            user.save()

            return redirect('profile-settings')
    return render(request, 'profile_config.html')

@login_required(login_url='login')
def preferForm(request):
    if request.method == 'POST':
        form = PreferForm(request.POST)

        if form.is_valid():
            user = Usuario.objects.get(id=request.user.id)
            user.profile_color = form.cleaned_data['profile_color']
            user.adult_content = form.cleaned_data['adult_content']
            user.save()

            return redirect('profile-settings')
    return render(request, 'profile_config.html')

@login_required(login_url='login')
def accountForm(request):
    if request.method == 'POST':
        if request.POST.get('pass_1') and request.POST.get('pass_2'):
            if request.user.email == request.POST.get('email'):
                form = AccountPasswordForm(request.POST)
                
                if passwordForm(form):
                    user = Usuario.objects.get(id=request.user.id)
                    user.password = make_password(form.cleaned_data['pass_1'])
                    user.save()
                    return redirect('profile-settings')
            else:
                return render(request, 'profile_config.html', {'pillo':'Eres un pillo, ¿eh?'})
        else:
            form = AccountEmailForm(request.POST)
            
            if emailForm(form):
                user = Usuario.objects.get(id=request.user.id)
                user.email = form.cleaned_data['email']
                user.save()
                return redirect('profile-settings')
            
    return render(request, 'profile_config.html')

def emailForm(form):
    if form.is_valid():
        if form.nada():
            if form.check_email():
                return True            
            else:
                return render(request, 'profile_config.html', {'email':'El correo electrónico ya está en uso'})
        else:
            return render(request, 'profile_config.html', {'email_nada':'Este campo no puede estar vacío'})
    else:
        return render(request, 'profile_config.html', {'email_valid':'Tiene que ser un correo electrónico válido'})

def passwordForm(form):
    if form.is_valid():
        if form.nada():
            if form.check_password():
                return True
            else:
                return render(request, 'profile_config.html', {'pass':'Las contraseñas deben ser iguales'})
        else:
                return render(request, 'profile_config.html', {'pass_nada':'Este campo no puede estar vacío'})
    else:
        return render(request, 'profile_config.html', {'pass_valid':'Tiene que ser una contraseña válida'})