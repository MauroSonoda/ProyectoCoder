from django.shortcuts import render
from .models import Curso,Profesor,Estudiante
from django.http import HttpResponse,HttpRequest
from .forms import CursoFormulario,ProfesorFormulario,EstudianteFormulario
from django.views.generic.list import ListView #me va a permitir listar 
from django.views.generic.detail import DetailView#mostar el detalle
from django.views.generic.edit import DeleteView,CreateView#eliminar,crear y act nuevo registro
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
    
class CursoDetail(LoginRequiredMixin,DetailView): #anula el mixin (para anular funcionalidades)
    model = Curso
    template_name = "curso_detail.html"
    context_object_name="curso"
class CursoCreate(LoginRequiredMixin,CreateView):
    model = Curso
    template_name = "curso_create.html"
    fields=["nombre","camada"]
    success_url="/app-coder/"
    
class CursoDelete(LoginRequiredMixin,DeleteView):
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
def sobremi(req):
    return render(req,"sobremi.html")
def loginView(req): #crea la sesion en la plataforma
    if req.method == 'POST':
        miFormulario=AuthenticationForm(req, data=req.POST)
        
        if miFormulario.is_valid():
            
            data=miFormulario.cleaned_data
            usuario=data["username"]
            psw=data["password"]
            user=authenticate(username=usuario,password=psw)
            if user:#si no es none
                login(req, user)
                return render(req,"inicio.html",{"mensaje": f" bienvenido {usuario}"})
            else:
                return render(req,"inicio.html",f"Datos incorrectos")
        else: 
            return render(req,"inicio.html",{"mensaje": "formulario invalido"})
    else:
         miFormulario=AuthenticationForm()
         return render(req,"login.html",{"miFormulario": miFormulario})
def register(req): #registro de nuevo usario
    if req.method == 'POST':
        miFormulario=UserCreationForm(req.POST)
        if miFormulario.is_valid():
            
            data=miFormulario.cleaned_data
            
            usuario=data["username"]
            
            miFormulario.save()
            
            return render(req,"inicio.html",{"mensaje": f"usuario {usuario} creado con exito"})
        else:   
            return render(req,"inicio.html",{"mensaje": "formulario invalido"})
    else:
         miFormulario=UserCreationForm()
         return render(req,"registro.html",{"miFormulario": miFormulario})
