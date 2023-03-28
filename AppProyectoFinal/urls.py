from django.urls import path
from AppProyectoFinal.views import soy, mostrar_formulario_de_buscar_curso, lista_de_profesores, lista_de_cursos, lista_de_estudiantes, mostrar_formulario_curso, mostrar_formulario_estudiante

urlpatterns = [
    path('quien_soy/', soy, name="AppProyectoFinalquiensoy"),
    path('cursos/buscar', mostrar_formulario_de_buscar_curso, name="AppProyectoFinalBuscar"),
    path('cursos/', lista_de_cursos, name="AppProyectoFinallistacursos"),
    path('cursos/solicitar/', mostrar_formulario_curso, name="AppProyectoFinalSolicitar"),
    path('profesores/', lista_de_profesores, name="AppProyectoFinallistaprofesores"),
    path('estudiantes/', lista_de_estudiantes, name="AppProyectoFinallistaestudiantes"),
    path('estudiantes/registrar/', mostrar_formulario_estudiante, name="AppProyectoFinalRegistrarEstudiante"),
]