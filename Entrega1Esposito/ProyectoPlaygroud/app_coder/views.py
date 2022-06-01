from django.shortcuts import render
from django.http import *
from django.template import loader
import datetime
from app_coder.models import Entregable
from app_coder.models import Cursos, Estudiante, Profesor
from app_coder.forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def estudiantes(request):
    estudiante = Estudiante.objects.all()
    bdestudiantes={"bdestudiantes": estudiante}
    return render(request,'estudiantes.html',bdestudiantes)

def profesores(request):
    profe= Profesor.objects.all()
    bdprofe={"bdprofe": profe}
    return render(request,'profesores.html',bdprofe)

def entregas(request):
    entrega=Entregable.objects.all()
    bdentregas={"bdentregas": entrega}
    return render(request,'entregables.html',bdentregas)

def cursos(request):
    curso = Cursos.objects.all()
    bdcursos={"bdcursos": curso}
    plantilla = loader.get_template("cursos.html")
    vistacursos= plantilla.render(bdcursos)
    return HttpResponse(vistacursos)

def biografia(request):
    return render(request,'biografia.html')

def formaltas(request):
    return render (request, 'formaltas.html')

def altasAlumnos(request):
    if request.method=='POST':

        mi_formulario = Estudiante_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data

            estudiantes=Estudiante(nombre=datos['nombre'], apellido=datos['apellido'], email=datos['email'])
            estudiantes.save()
            texto=f"Se guardo en la BD al Estudiante: {estudiantes.nombre} {estudiantes.apellido}"
            return HttpResponse(texto)

def altasCursos(request):
    if request.method=='POST':

        mi_formulario1 = Cursos_formulario(request.POST)
        if mi_formulario1.is_valid():
            datos1=mi_formulario1.cleaned_data

            curso= Cursos(nombre=datos1['nombre'],comision=datos1['comision'])
            curso.save()
            texto=f"Se guardo en la BD al Curso: {curso.nombre} Comision: {curso.comision}"
            return HttpResponse(texto)

def altasProfesores(request):
    if request.method=='POST':

        mi_formulario2= Profesor_formulario(request.POST)
        if mi_formulario2.is_valid():
            datos2=mi_formulario2.cleaned_data

            profesores=Profesor(nombre=datos2['nombre'],apellido=datos2['apellido'],email=datos2['email'],profesion=datos2['profesion'])
            profesores.save()
            texto=f"Se guardo en la BD al Profesor: {profesores.nombre} {profesores.apellido} Profesion: {profesores.profesion}"
            return HttpResponse(texto)
         
def altasEntregas(request):
    if request.method=='POST':
        entrega=Entregable(nombre=request.POST['nombre'], FechaDeEntrega='2022-05-31', entregado='True')
        entrega.save()
        texto=f"Se entregó el trabajo de:{entrega.nombre}"
        return HttpResponse(texto)

def busca(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        entrega=Entregable.objects.filter(nombre__icontains= nombre)
        return render (request,'entregas.html',{"entrega":entrega})
    else:
        return HttpResponse("Campos Vacios o Incorrecto")
