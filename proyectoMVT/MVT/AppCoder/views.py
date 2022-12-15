from django.shortcuts import render
from .models import  Papa
from django.http import HttpResponse

# Create your views here.

def familia(request):

    familiares= Papa(nombre="Nicolas", edad=74)
    familiares.save()
    cadena_texto="familia guardada: Nombre: "+familiares.nombre+" "+str(familiares.edad)

    
    return HttpResponse(cadena_texto)

def familia2(request):

    familiares= Papa(nombre="Mirta", edad=68)
    familiares.save()
    cadena_texto="familia guardada: Nombre: "+familiares.nombre+" "+str(familiares.edad)

    
    return HttpResponse(cadena_texto)
  

def familia3(request):

    familiares= Papa(nombre="Caro", edad=35)
    familiares.save()
    cadena_texto="familia guardada: Nombre: "+familiares.nombre+" "+str(familiares.edad)

    
    return HttpResponse(cadena_texto)
  
