from django import forms

class Estudiante_formulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField(max_length=40)

class Profesor_formulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField(max_length=40)
    profesion=forms.CharField(max_length=40)

class Entregable_formulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    FechaDeEntrega=forms.DateField()
    entregado=forms.BooleanField()

class Cursos_formulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    comision=forms.IntegerField()