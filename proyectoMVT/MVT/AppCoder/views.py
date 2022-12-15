from django.shortcuts import render
from .models import Papa, Madre, Hermana
from django.http import HttpResponse 

# Create your views here. controladores en los views

def papa(request):

    papitos= Papa (nombre="Nicolas", apellido="Sciarra", edad=74, nacimiento="3 de abril 1945")
    papitos.save()
    cadena_texto=f"Nombre de familiares: Nombre: {papitos.nombre}, Apellido: {papitos.apellido}, Edad {papitos.edad}, Fecha de Nac: {papitos.nacimiento}"
    return HttpResponse(cadena_texto)

    
def mama(request):
    mamitas= Madre (nombre="Mirta", apellido="Riquelme", edad=70, nacimiento="30 de enero 1948")
    mamitas.save()
    cadena_texto=f"Nombre de familiares: Nombre: {mamitas.nombre}, Apellido: {mamitas.apellido}, Edad {mamitas.edad}, Fecha de Nac: {mamitas.nacimiento}"
    return HttpResponse(cadena_texto)

def hermana(request):
    hermanita= Hermana (nombre="Caro", apellido="Sciarra", edad=40, nacimiento="26 de septiembre")
    hermanita.save()
    cadena_texto=f"Nombre de familiares: Nombre: {hermanita.nombre}, Apellido: {hermanita.apellido}, Edad {hermanita.edad}, Fecha de Nac: {hermanita.nacimiento}"
    return HttpResponse(cadena_texto)