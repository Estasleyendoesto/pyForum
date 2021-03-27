from django import forms

class CreatePost(forms.Form):
    titulo = forms.CharField(max_length=70, required=True)
    adultos = forms.BooleanField(required=False)
    cuerpo = forms.CharField(widget=forms.Textarea, required=True)
    borrador = forms.BooleanField(required=False)

    def check_titulo(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')

        if titulo:
            return True
        else:
            raise forms.ValidationError("El título no puede estar vacío")

    