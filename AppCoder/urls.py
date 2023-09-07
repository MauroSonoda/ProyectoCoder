from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/',lista_cursos),
    path('',inicio,name='inicio'),
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
    path('listaCursos/',CursoList.as_view(),name="listacursos"),
    path('detalleCursos/<pk>',CursoDetail.as_view(),name="detallecursos"),
    path('creaCursos/',CursoCreate.as_view(),name="creacursos"),
    path('eliminaCursos/<pk>',CursoDelete.as_view(),name="eliminarcursos"),
    path('listaEstudiantes/',listaEstudiantes,name="listaEstudiantes"),
    path('creaEstudiante/',creaEstudiante,name="creaEstudiantes"),
    path('editarEstudiante/<int:id>',editarEstudiante,name="editarEstudiante"),
    path('eliminaEstudiante/<int:id>',eliminarEstudiante,name="eliminarEstudiante"), 
]  