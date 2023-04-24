from django import forms
from AppProyectoFinal.models import Profesor

class CursoForm(forms.Form):
    title = forms.CharField(max_length=100, label="Título")
    intro = forms.CharField(max_length=300, label="Introducción", widget=forms.Textarea)
    subtitle = forms.CharField(max_length=100, label="Subtítulo")
    body = forms.CharField(max_length=1000, label="Desarrollo", widget=forms.Textarea)
    image = forms.ImageField(label="Imagen", required=False)

class ComentarioForm(forms.Form):
    cuerpo = forms.CharField(max_length=100, label="Comentario", widget=forms.Textarea)

class EstudianteForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=40)
    apellido = forms.CharField(min_length=3, max_length=40)
    email = forms.EmailField()

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = "__all__"

class BuscarCursoForm(forms.Form):
    title = forms.CharField(label="Título")
