from django.shortcuts import render
from .models import Papa
from django.http import HttpResponse

# Create your views here.
def familia(request):

    familiares= Papa(nombre="Nicolas", apellido="Sciarra")
    familiares.save()
    cadena_texto=f"famialia guardada: Nombre: {familiares.nombre}"
    
    return HttpResponse(cadena_texto)


