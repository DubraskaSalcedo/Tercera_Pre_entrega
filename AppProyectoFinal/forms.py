from django import forms
from AppProyectoFinal.models import Profesor
class CursoForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=40)
    grupo = forms.IntegerField(min_value=10)

class EstudianteForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=40)
    apellido = forms.CharField(min_length=3, max_length=40)
    email = forms.EmailField()

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields ="__all__"

class BuscarCursoForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=40)