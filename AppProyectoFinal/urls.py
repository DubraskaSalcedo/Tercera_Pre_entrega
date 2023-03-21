from django.urls import path
from ProyectoFinal.views import soy, lista_de_profesores, lista_de_cursos, lista_de_estudiantes, mostrar_formulario_curso, mostrar_formulario_estudiante

urlpatterns = [
    path('quien_soy/', soy, name="AppProyectoFinalquiensoy"),
    path('cursos/', lista_de_cursos, name="AppProyectoFinallistacursos"),
    path('cursos/solicitar/', mostrar_formulario_curso, name="AppProyectoFinalSolicitar"),
    path('profesores/', lista_de_profesores, name="AppProyectoFinallistaprofesores"),
    path('estudiantes/', lista_de_estudiantes, name="AppProyectoFinallistaestudiantes"),
    path('estudiantes/registrar/', mostrar_formulario_estudiante, name="AppProyectoFinalRegistrarEstudiante"),
]