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

]