from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.
def curso(req,nombre,camada):
    curso=Curso(nombre=nombre,camada=camada)
    curso.save()
    return HttpResponse(f"curso {curso.nombre} camada: {curso.camada}creado")
def lista_cursos(req):
    lista=Curso.objects.all()
    return render(req,"lista_cursos.html",{"lista_cursos":lista})#lista_cursos es la variable para que recorra en el template