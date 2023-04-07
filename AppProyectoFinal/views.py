from django.shortcuts import render, redirect
from AppProyectoFinal.models import Curso, Estudiante, Profesor
from AppProyectoFinal.forms import CursoForm, EstudianteForm, BuscarCursoForm, ProfesorForm
from django.contrib.auth.decorators import login_required
def mostrar_principal(request):
    return render(request,"base.html")

def soy(request):
    return render(request, "AppProyectoFinal/quien_soy.html")

def lectura_completa(request):
    pass
def lista_de_cursos(request):
    all_cursos = Curso.objects.all()
    context = {"todos_los_cursos": all_cursos}
    return render(request, "AppProyectoFinal/lista_de_cursos.html", context=context)

def mostrar_formulario_curso(request):
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(nombre=informacion['nombre'], grupo=informacion['grupo'])
            curso_save.save()
            context = {"curso": curso_save}
            return render(request, "AppProyectoFinal/guardar_curso.html", context=context)
    context = {"form": CursoForm()}
    return render(request, "AppProyectoFinal/crear_curso.html", context=context)

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

def mostrar_formulario_de_buscar_curso(request):
    if request.method == "GET":
        mi_formulario = BuscarCursoForm(request.GET)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion['nombre'])
            context = {"cursos": cursos_filtrados}
            return render(request, "AppProyectoFinal/listar_filtro.html", context=context)
        context = {"form": BuscarCursoForm()}
    return render(request, "AppProyectoFinal/buscar_curso.html", context=context)

@login_required
def eliminar_curso(request, grupo):
    get_curso= Curso.objects.get(grupo=grupo)
    get_curso.delete()
    return redirect("AppProyectoFinallistacursos")
def editar_curso(request, grupo):
    get_curso = Curso.objects.get(grupo=grupo)
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            get_curso.nombre = informacion['nombre']
            get_curso.grupo = informacion['grupo']
            get_curso.save()
            return redirect("AppProyectoFinallistacursos")
    context = {"grupo": grupo, "form": CursoForm(initial={"nombre": get_curso.nombre, "grupo": get_curso.grupo})}
    return render(request, "AppProyectoFinal/editar_curso.html", context=context)

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
