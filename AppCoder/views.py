from django.shortcuts import render
from .models import Curso,Profesor,Estudiante
from django.http import HttpResponse,HttpRequest
from .forms import CursoFormulario,ProfesorFormulario,EstudianteFormulario
from django.views.generic.list import ListView #me va a permitir listar 
from django.views.generic.detail import DetailView#mostar el detalle
from django.views.generic.edit import DeleteView,CreateView#eliminar,crear y act nuevo registro

# Create your views here.
def curso(req,nombre,camada):
    curso=Curso(nombre=nombre,camada=camada)
    curso.save()
    return HttpResponse(f"curso {curso.nombre} camada: {curso.camada}creado")
def lista_cursos(req):
    lista=Curso.objects.all()
    return render(req,"lista_cursos.html",{"lista_cursos":lista})#lista_cursos es la variable para que recorra en el template
def inicio(req):
    return render(req,"inicio.html")
def cursos(req):
    return render(req,"cursos.html")
def profesores(req):
   return render(req,"profesores.html")
def estudiantes(req):
    return render(req,"estudiantes.html")
def entregables(req):
   return render(req,"entregables.html")
def curso_formulario(req:HttpRequest):
    if req.method == 'POST':
        miFormulario=CursoFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            
            curso=Curso(nombre=data["curso"],data=req.POST["camada"])
            curso.save()
            return render(req,"inicio.html",{"mensaje": "curso creado con exito"})
        else: 
            return render(req,"inicio.html",{"mensaje": "formulario invalido"})
    else:
        miFormulario=CursoFormulario()        
        return render(req,"cursoFormulario.html",{"miFormulario":miFormulario})
def busquedaCamda(req):
     return render(req,"busquedaCamada.html")
def buscar(req):
    if req.GET["camada"]:
        camada=req.GET["camada"]
        curso=Curso.objects.get(camada=camada)
        if curso:
            return render(req,"resultadobusqueda.html",{"curso":curso})
    else:
        return HttpResponse('no escribiste nada')
def listaprofesores(req):
    profesores = Profesor.objects.all()
    return render(req,"leerProfesores.html",{"profesores":profesores})
def crea_profesor(req):
    if req.method == 'POST':
        miFormulario=ProfesorFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            
            profesor=Profesor(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],profesion=data["profesion"])
            profesor.save()
            return render(req,"inicio.html",{"mensaje": "Profesor creado con exito"})
        else: 
            return render(req,"inicio.html",{"mensaje": "formulario invalido"})
    else:
        miFormulario=ProfesorFormulario()        
        return render(req,"profesorFormulario.html",{"miFormulario":miFormulario})
def eliminarProfesor(req, id):
    if req.method =='POST':
        
        profesor=Profesor.objects.get(id=id)
        profesor.delete()
        
        profesores = Profesor.objects.all()
        return render(req,"leerProfesores.html",{"profesores":profesores})
def editarProfesor(req,id):
    profesor=Profesor.objects.get(id=id)
    
    if req.method == 'POST':
        miFormulario=ProfesorFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            #sobreescribo
            profesor.nombre=data["nombre"]
            profesor.apellido=data["apellido"]
            profesor.email=data["email"]
            profesor.profesion=data["profesion"]
            
            profesor.save() #guardo
            return render(req,"inicio.html",{"mensaje": "Profesor actualizado con exito"})
        else: 
            return render(req,"inicio.html",{"mensaje": "formulario invalido"})
    else:
        miFormulario=ProfesorFormulario(initial={
            "nombre":profesor.nombre,
            "apellido":profesor.apellido,
            "email":profesor.email,
            "profesion":profesor.profesion,
            
            }) #no puede estar vacio #si abro con metodo get viene aca       
        return render(req,"editarProfesor.html",{"miFormulario":miFormulario,"id": profesor.id })
#recuperar todo los cursos y rendrizo en un html
class CursoList(ListView):#eredo
    model= Curso
    template_name="curso_list.html" 
    context_object_name="cursos"
    
class CursoDetail(DetailView):
    model = Curso
    template_name = "curso_detail.html"
    context_object_name="curso"
class CursoCreate(CreateView):
    model = Curso
    template_name = "curso_create.html"
    fields=["nombre","camada"]
    success_url="/app-coder/"
    
class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_delete.html"
    success_url="/app-coder/"
    
def listaEstudiantes(req):
    estudiantes = Estudiante.objects.all()
    return render(req,"estudiante_list.html",{"estudiante":estudiantes})
def creaEstudiante(req):
    if req.method == 'POST':
        miFormulario=EstudianteFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            
            estudiante=Estudiante(nombre=data["nombre"],apellido=data["apellido"],email=data["email"])
            estudiante.save()
            return render(req,"inicio.html",{"mensaje": "estudiante creado con exito"})
        else: 
            return render(req,"inicio.html",{"mensaje": "formulario invalido"})
    else:
        miFormulario=EstudianteFormulario()        
        return render(req,"estudianteFormulario.html",{"miFormulario":miFormulario})
    
def editarEstudiante(req,id):
    estudiante=Estudiante.objects.get(id=id)
    
    if req.method == 'POST':
        miFormulario=EstudianteFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            #sobreescribo
            estudiante.nombre=data["nombre"]
            estudiante.apellido=data["apellido"]
            estudiante.email=data["email"]
            estudiante.save() #guardo
            
            return render(req,"inicio.html",{"mensaje": "editado con exito"})
        else: 
            return render(req,"inicio.html",{"mensaje": "formulario invalido"})
    else:
        miFormulario=EstudianteFormulario(initial={
            "nombre":estudiante.nombre,
            "apellido":estudiante.apellido,
            "email":estudiante.email,
            })     
        return render(req,"editarEstudiante.html",{"miFormulario":miFormulario,"id": estudiante.id })
def eliminarEstudiante(req,id):
      if req.method =='POST':
        
        estudiante=Estudiante.objects.get(id=id)
        estudiante.delete()
        
        estudiante = Estudiante.objects.all()
        return render(req,"estudiante_list.html",{"estudiante":estudiante})