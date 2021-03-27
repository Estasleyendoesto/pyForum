from django import forms

class ComentarioForm(forms.Form):
    comentario = forms.CharField(widget=forms.Textarea, required=True, help_text="El comentario no puede estar en blanco")

    def check_comentario(self):
        cleaned_data = super().clean()
        comentario = cleaned_data.get('comentario')

        if comentario:
            return True
        else:
            self.add_error('comentario', "El comentario no puede estar en blanco")