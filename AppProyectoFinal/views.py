from django.shortcuts import render, redirect
from AppProyectoFinal.models import Estudiante, Profesor, Curso3, Comentario
from AppProyectoFinal.forms import CursoForm, ComentarioForm, EstudianteForm, BuscarCursoForm, ProfesorForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
def mostrar_principal(request):
    return render(request,"base.html")

def soy(request):
    return render(request, "AppProyectoFinal/quien_soy.html")

def lista_de_cursos(request):
    all_cursos = Curso3.objects.all()
    context = {"todos_los_cursos": all_cursos}
    return render(request, "AppProyectoFinal/lista_de_cursos.html", context=context)

def mostrar_formulario_curso(request):
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)
        usuario = request.user
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            fecha = datetime.now()
            curso_save = Curso3(
                title=informacion['title'],
                intro=informacion['intro'],
                subtitle=informacion['subtitle'],
                author=usuario,
                body=informacion['body'],
                fecha=fecha
            )
            curso_save.save()
            context = {"curso": curso_save}
            return render(request, "AppProyectoFinal/guardar_curso.html", context=context)
    context = {"form": CursoForm()}
    return render(request, "AppProyectoFinal/crear_curso.html", context=context)

def mostrar_formulario_de_buscar_curso(request):
    if request.method == "GET":
        mi_formulario = BuscarCursoForm(request.GET)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cursos_filtrados = Curso3.objects.filter(title__icontains=informacion['title'])
            context = {"cursos": cursos_filtrados}
            return render(request, "AppProyectoFinal/listar_filtro.html", context=context)
        context = {"form": BuscarCursoForm()}
    return render(request, "AppProyectoFinal/buscar_curso.html", context=context)

def eliminar_curso(request, title):
    get_curso= Curso3.objects.get(title=title)
    get_curso.delete()
    return redirect("AppProyectoFinallistacursos")

def editar_curso(request, title):
    get_curso = Curso3.objects.get(title=title)
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_curso.title = informacion['title']
            get_curso.intro = informacion['intro']
            get_curso.subtitle = informacion['subtitle']
            get_curso.body = informacion['body']
            get_curso.save()
            return redirect("AppProyectoFinallistacursos")
    context = {"title": get_curso.title, "form": CursoForm(initial={
            "title": get_curso.title,
            "intro": get_curso.intro,
            "subtitle": get_curso.subtitle,
            "body": get_curso.body
        }
        )
    }
    return render(request, "AppProyectoFinal/editar_curso.html", context=context)

def mostrar_detalles_de_curso(request, title):
    get_curso = Curso3.objects.get(title=title)
    all_comments = Comentario.objects.filter(curso3=get_curso)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nuevo_comentario = Comentario(curso3=get_curso, cuerpo=informacion['cuerpo'],
                                          autor=request.user.username)
            nuevo_comentario.save()
    contexto = {"form":ComentarioForm(), "title": title, "curso": get_curso, "all_comments":all_comments}
    return render(request, "AppProyectoFinal/detalles_de_curso.html", context=contexto)

def mostrar_formulario_profesor(request):
    if request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor_save = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor_save.save()
            context = {"profesor": profesor_save}
            return render(request, "AppProyectoFinal/guardar_profesor.html", context=context)
    context = {"form": ProfesorForm()}
    return render(request, "AppProyectoFinal/registrar_profesor.html", context=context)
def lista_de_profesores(request):
    all_profesores = Profesor.objects.all()
    context = {"todos_los_profesores": all_profesores}
    return render(request, "AppProyectoFinal/lista_de_profesores.html", context=context)

def lista_de_estudiantes(request):
    all_estudiantes = Estudiante.objects.all()
    context = {"todos_los_estudiantes": all_estudiantes}
    return render(request, "AppProyectoFinal/lista_de_estudiantes.html", context=context)

def mostrar_formulario_estudiante(request):
    if request.method == "POST":
        mi_formulario = EstudianteForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiante_save = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante_save.save()
            context = {"estudiante": estudiante_save}
            return render(request, "AppProyectoFinal/guardar_estudiante.html", context=context)
    context = {"form": EstudianteForm()}

    return render(request, "AppProyectoFinal/registrar_estudiante.html", context=context)
