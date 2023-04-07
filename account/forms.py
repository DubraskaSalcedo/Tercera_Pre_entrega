from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    is_staff = forms.BooleanField()
    imagen = forms.ImageField()
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "is_staff", "imagen")
