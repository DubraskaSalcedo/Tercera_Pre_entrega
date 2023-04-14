from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserEditForm(forms.Form):
    first_name = forms.CharField(max_length=20, label="Nombre")
    last_name = forms.CharField(max_length=20, label="Apellido")
    email = forms.EmailField()
    is_staff = forms.BooleanField(label="En staff")
    imagen = forms.ImageField(label="Imagen")


