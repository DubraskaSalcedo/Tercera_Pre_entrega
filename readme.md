Tenemos una **WEB Django con patrón MVT**:
Destacamos las siguientes características:
Tenemos tres clases en _models.html_, a saber, Curso, Estudiante, 
Profesor; tres formularios en forms.html, que son CursoForm, EstudianteForm 
y BuscarCursoForm, una aplicación llamada AppProyectoFinal, dentro de la cual resaltamos:
* una función de registro de cursos a la cual accedemos por el botón que está en la barra de navegación "Cursos", haciendo click en el link "Solicitar Curso"; que nos muestra un formulario con los items obligatorios Curso y Grupo, y el botón "Crear", al llenar el formulario y dar click en "Crear", se guarda el curso
        y nos sale un mensaje de confirmación.
* una función de registro de estudiantes a la cual accedemos por el botón que está en la barra de navegación "Estudiantes", haciendo click en el link "Registrar";  que nos muestra un formulario con los items obligatorios Nombre, Apellido y Correo, y el botón "Registrar" al llenar el formulario y dar click en "Registrar", se guarda el estudiante y nos sale un mensaje de confirmación.
* una función de búsqueda de cursos a la cual accedemos por el botón que está en la barra de navegación "Cursos", haciendo click en el link "Bucar Curso"; que nos muestra un formulario con un único item obligatorio Nombre y el botón "Buscar", al llenar este campo y dar click en "Buscar" nos lleva o bien a la lista de los resultados de la búsqueda o nos da un mensaje de que no existen cursos correspondientes a la búsqueda.


Usamos una plantilla base, base.html, que está en la carpeta templates y los demás que usamos en las views están dentro de la carpeta AppProyectoFinal junto a base.html.


