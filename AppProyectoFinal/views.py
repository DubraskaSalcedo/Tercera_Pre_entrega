from django.shortcuts import render, redirect
from AppProyectoFinal.models import Comentario, Taller
from AppProyectoFinal.forms import CursoForm, ComentarioForm, BuscarCursoForm
from datetime import datetime

def mostrar_principal(request):
    return render(request,"base.html")

def soy(request):
    return render(request, "AppProyectoFinal/quien_soy.html")

def lista_de_talleres(request):
    all_talleres = Taller.objects.all()
    context = {"todos_los_talleres": all_talleres}
    return render(request, "AppProyectoFinal/lista_de_talleres.html", context=context)
def mostrar_detalles_de_taller(request, title):
    get_curso = Taller.objects.get(title=title)
    all_comments = Comentario.objects.filter(taller=get_curso)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nuevo_comentario = Comentario(taller=get_curso, cuerpo=informacion['cuerpo'], autor=request.user)
            nuevo_comentario.save()
    contexto = {"form":ComentarioForm(), "title": title, "curso": get_curso, "all_comments":all_comments}
    return render(request, "AppProyectoFinal/detalles_de_taller.html", context=contexto)

def mostrar_formulario_taller(request):
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST, request.FILES)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Taller(
                title=informacion['title'],
                intro=informacion['intro'],
                subtitle=informacion['subtitle'],
                body=informacion['body'],
                author=request.user,
                fecha=datetime.now(),
                image=informacion['image']
            )
            curso_save.save()
            context = {"curso": curso_save}
            return render(request, "AppProyectoFinal/guardar_curso.html", context=context)
    context = {"form": CursoForm()}
    return render(request, "AppProyectoFinal/crear_curso.html", context=context)

def mostrar_formulario_de_buscar_taller(request):
    if request.method == "GET":
        mi_formulario = BuscarCursoForm(request.GET)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cursos_filtrados = Taller.objects.filter(title__icontains=informacion['title'])
            context = {"cursos": cursos_filtrados}
            return render(request, "AppProyectoFinal/listar_filtro_taller.html", context=context)
        context = {"form": BuscarCursoForm()}
    return render(request, "AppProyectoFinal/buscar_taller.html", context=context)
def eliminar_taller(request, title):
    get_curso= Taller.objects.get(title=title)
    get_curso.delete()
    return redirect("AppProyectoFinalListaTalleres")

def editar_taller(request, title):
    get_curso = Taller.objects.get(title=title)
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST, request.FILES)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_curso.title = informacion['title']
            get_curso.intro = informacion['intro']
            get_curso.subtitle = informacion['subtitle']
            get_curso.body = informacion['body']
            if informacion['image'] == None:
                get_curso.save()
            else:
                get_curso.image = informacion['image']
                get_curso.save()
            return redirect("AppProyectoFinalListaTalleres")
    context = {"title": get_curso.title, "form": CursoForm(initial={
            "title": get_curso.title,
            "intro": get_curso.intro,
            "subtitle": get_curso.subtitle,
            "body": get_curso.body,
            "image": get_curso.image
        }
        )
    }
    return render(request, "AppProyectoFinal/editar_curso.html", context=context)