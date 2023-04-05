from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.

def login_account(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = authenticate(username=informacion['username'], password=informacion['password'])
            print(user)
            if user:
                login(request, user)
                return render(request, "account/prueba.html")
            else:
                return redirect("AppProyectoFinallistacursos")
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "account/login.html", context=context)

def logout_account(request):
    pass

def register_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accountLogin")
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "account/register.html", context=context)