from django.shortcuts import render
from .models import  Papa

# Create your views here. controladores en los views

def familia(request):

    familiares= Papa(nombre="Nicolas", edad=74)
    familiares.save()
    cadena_texto="familia guardada: Nombre: "+familiares.nombre+" "+str(familiares.edad)

    
    return HttpResponse(cadena_texto)


    familiares.save()
    cadena_texto="familia guardada: Nombre: "+familiares.nombre+" "+str(familiares.edad)

    
    return HttpResponse(cadena_texto)
  
