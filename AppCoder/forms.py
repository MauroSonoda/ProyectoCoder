from django import forms
#formulario para base de dato
class CursoFormulario(forms.Form):
   curso=forms.CharField(required=True)
   camada=forms.IntegerField(required=True)


class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(required=True)
    apellido=forms.CharField(required=True)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=30)
    
class EstudianteFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
