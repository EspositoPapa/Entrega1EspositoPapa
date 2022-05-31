from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('inicio',views.index),
    path('estudiantes',views.estudiantes, name="estudiantes"),
    path('profesores',views.profesores,name="profesores"),
    path('cursos',views.cursos, name="cursos"),
    path('entregas',views.entregas, name="entregas"),
    path('altasCursos',views.altasCursos),
    path('altasAlumnos',views.altasAlumnos),
    path('altasProfesores',views.altasProfesores),
    path('altasEntregas',views.altasEntregas),
    path('altas', views.formaltas, name="altas"),
    path('biografia',views.biografia, name='biografia'),
    path('busca',views.busca, name='busca')
]
 #nombre, apellido, email, profesion, comision