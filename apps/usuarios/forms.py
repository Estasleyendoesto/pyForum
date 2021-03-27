from django import forms
from django.contrib.auth import authenticate
from .models import Usuario

class RegistroUsuario(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    pass_1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    pass_2 = forms.CharField(widget=forms.PasswordInput, label='Repite tu contraseña')

    def check_username(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        user = Usuario.objects.filter(username=username)

        if not user:
            return True
        else:
            self.add_error('username', "El nombre de usuario está ocupado")

    def check_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        user = Usuario.objects.filter(email=email)

        if not user:
            return True
        else:
            self.add_error('email', "El correo electrónico está siendo usado")

    def check_password(self):
        cleaned_data = super().clean()
        pass_1 = cleaned_data.get('pass_1')
        pass_2 = cleaned_data.get('pass_2')

        if pass_1 == pass_2:
            return True
        else:
            self.add_error('pass_1', "")
            self.add_error('pass_2', "Las contraseñas deben coincidir")

    def nada(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        pass_1 = cleaned_data.get('pass_1')
        pass_2 = cleaned_data.get('pass_2')

        if username and email and pass_1 and pass_2:
            return True
        else:
            raise forms.ValidationError('Ningún campo debe estar vacío')

class LoginUsuario(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

    def check_user(self, request):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            return user
        else:
            raise forms.ValidationError('El email o la contraseña son incorrectos')

    def nada(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            return True
        else:
            raise forms.ValidationError('Ningún campo debe estar vacío')

class PersonalForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    frase = forms.CharField(max_length=250, required=False)
    imagen = forms.ImageField(required=False)

class PreferForm(forms.Form):
    profile_color = forms.CharField(max_length=30, required=False)
    adult_content = forms.BooleanField(required=False)

class AccountEmailForm(forms.Form):
    email = forms.EmailField(required=True)

    def nada(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if email:
            return True
        else:
            return False

    def check_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        user = Usuario.objects.filter(email=email)

        if not user:
            return True
        else:
            return False

class AccountPasswordForm(forms.Form):
    pass_1 = forms.CharField(widget=forms.PasswordInput, required=True)
    pass_2 = forms.CharField(widget=forms.PasswordInput, required=True)

    def nada(self):
        cleaned_data = super().clean()
        pass_1 = cleaned_data.get('pass_1')
        pass_2 = cleaned_data.get('pass_2')

        if pass_1 and pass_2:
            return True
        else:
            return False

    def check_password(self):
        cleaned_data = super().clean()
        pass_1 = cleaned_data.get('pass_1')
        pass_2 = cleaned_data.get('pass_2')

        if pass_1 == pass_2:
            return True
        else:
            return False

    