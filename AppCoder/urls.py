from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/',lista_cursos),
    path('',inicio),
    path('cursos/',cursos,name='Cursos'),
    path('profesores/',profesores,name='Profesores'),
    path('estudiantes/',estudiantes,name='Estudiantes'),
    path('entregables/',entregables,name='Entregables'),
    path('curso-formulario/',curso_formulario,name='cursoFormulario'),
    path('busqueda-camada/',busquedaCamda,name='BusquedaCamada'),
    path('buscar/',buscar,name="Buscar"),
    path('listaProfesores/',listaprofesores,name="listaprofesores"),
    path('creaProfesores/',crea_profesor,name="CreaProfesores"),
    path('eliminaProfesor/<int:id>',eliminarProfesor,name="EliminaProfesores"),
    path('editarProfesor/<int:id>',editarProfesor,name="editarProfesor"),
] 