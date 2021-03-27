from django import forms
from .models import Etiqueta

class AddEtiqueta(forms.Form):
    nombre = forms.CharField(max_length=50, help_text='El nombre no puede estar vacío')
    imagen = forms.ImageField(help_text='La etiqueta debe tener una imagen')
    adulto = forms.BooleanField(required=False)

    def nada(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        imagen = cleaned_data.get('imagen')

        if nombre and imagen:
            return True
        else:
            raise forms.ValidationError('Tanto el nombre como la imagen no pueden estar vacíos')

    def check_nombre(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')

        etiqueta = Etiqueta.objects.filter(nombre__icontains=nombre)

        if not etiqueta:
            return True
        else:
            self.add_error('nombre', "Ya existe una etiqueta con el mismo nombre")