from django.urls import path
from AppProyectoFinal.views import*
urlpatterns = [
    path('quien_soy/', soy, name="AppProyectoFinalquiensoy"),
    path('talleres/', lista_de_talleres, name="AppProyectoFinalListaTalleres"),
    path('talleres/crear/', mostrar_formulario_taller, name="AppProyectoFinalCrearTaller"),
    path('talleres/buscar', mostrar_formulario_de_buscar_taller, name="AppProyectoFinalBuscarTaller"),
    path('talleres/editar/<title>/', editar_taller, name="AppProyectoFinalEditarTaller"),
    path('talleres/<title>/', mostrar_detalles_de_taller, name="AppProyectoFinalListaTalleresDetalles"),
    path('talleres/eliminar/<title>/', eliminar_taller, name="AppProyectoFinalEliminarTaller"),
    path('cursos/<title>/', mostrar_detalles_de_curso, name="AppProyectoFinallistacursosDetalles"),
    path('cursos/buscar', mostrar_formulario_de_buscar_curso, name="AppProyectoFinalBuscar"),
    path('cursos/', lista_de_cursos, name="AppProyectoFinallistacursos"),
    path('cursos/crear/', mostrar_formulario_curso, name="AppProyectoFinalSolicitar"),
    path('cursos/eliminar/<title>/', eliminar_curso, name="AppProyectoFinalEliminar"),
    path('cursos/editar/<title>/', editar_curso, name="AppProyectoFinalEditar"),
    #path('profesores/', lista_de_profesores, name="AppProyectoFinallistaprofesores"),
    #path('estudiantes/', lista_de_estudiantes, name="AppProyectoFinallistaestudiantes"),
    #path('estudiantes/registrar/', mostrar_formulario_estudiante, name="AppProyectoFinalRegistrarEstudiante"),
    #path('profesores/registrar/', mostrar_formulario_profesor, name="AppProyectoFinalRegistrarProfesor"),
]