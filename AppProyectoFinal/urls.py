from django.urls import path
from AppProyectoFinal.views import*
urlpatterns = [
    path('quien_soy/', soy, name="AppProyectoFinalquiensoy"),
    path('cursos/buscar', mostrar_formulario_de_buscar_curso, name="AppProyectoFinalBuscar"),
    path('cursos/', lista_de_cursos, name="AppProyectoFinallistacursos"),
    path('cursos/solicitar/', mostrar_formulario_curso, name="AppProyectoFinalSolicitar"),
    path('cursos/eliminar/<grupo>/', eliminar_curso, name="AppProyectoFinalEliminar"),
    path('cursos/editar/<grupo>/', editar_curso, name="AppProyectoFinalEditar"),
    path('profesores/', lista_de_profesores, name="AppProyectoFinallistaprofesores"),
    path('estudiantes/', lista_de_estudiantes, name="AppProyectoFinallistaestudiantes"),
    path('estudiantes/registrar/', mostrar_formulario_estudiante, name="AppProyectoFinalRegistrarEstudiante"),
    path('profesores/registrar/', mostrar_formulario_profesor, name="AppProyectoFinalRegistrarProfesor"),
]