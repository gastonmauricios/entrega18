from django.shortcuts import render
from .models import Papa
from django.http import HttpResponse

# Create your views here.

def familia(request):

    familiares= Papa(nombre="Nicolas", edad=74)
    familiares.save()
    cadena_texto="famialia guardada: Nombre: "+familiares.nombre+" "+str(familiares.edad)
    
    return HttpResponse(cadena_texto)


