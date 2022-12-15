from django.shortcuts import render
from .models import Papa
from django.http import HttpResponse 

# Create your views here. controladores en los views

def papa(request):

    papitos= Papa (nombre="Nicolas", apellido="Sciarra", edad=74, nacimiento="3 de abril 1945")
    cadena_texto=f"Nombre de familiares: Nombre: {papitos.nombre}, Apellido: {papitos.apellido}, Edad {papitos.edad}, Fecha de Nac: {papitos.nacimiento}"
    return HttpResponse(cadena_texto)
    
