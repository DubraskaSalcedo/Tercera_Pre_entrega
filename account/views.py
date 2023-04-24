from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from account.forms import UserEditForm
from account.models import Avatar
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login_account2(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user:
                login(request, user)
                return render(request, "account/prueba.html")
            else:
                return redirect("AppProyectoFinallistacursos")
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "account/login.html", context=context)

def login_account(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user:
                login(request, user)
                return render(request, "account/prueba.html")
            else:
                return redirect("AppProyectoFinallistacursos")
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "account/login.html", context=context)
def register_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accountLogin")
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "account/register.html", context=context)

def mi_perfil(request):
    usuario = request.user
    context={"usuario":usuario}
    return render(request, "account/mi_perfil.html", context=context)
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.email = informacion["email"]
            usuario.is_staff = informacion["is_staff"]
            try:
                usuario.avatar.imagen = informacion["imagen"]
                usuario.avatar.save()
            except:
                avatar = Avatar(user=usuario, imagen=informacion["imagen"])
                avatar.save()
            usuario.save()
            return redirect("AppProyectoFinallistacursos")
    try:
        image = usuario.avatar.imagen
    except Avatar.DoesNotExist:
        image = None
    form = UserEditForm(
        initial={
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
            "email": usuario.email,
            "is_staff": usuario.is_staff,
            "imagen": image
        }
    )
    context = {"form": form}
    return render(request, "account/editar_perfil.html", context=context)
