from django.http import HttpResponse #solicitud respuesta
import datetime
from django.template import Template, Context, loader

def saludar(request): # la solicitud que recibe del cliente es una request
    return HttpResponse("Hola Mundo !!!") #todo proyecto en django se comunica con el user a travez solicitud y recibe respuestas.

def segunda_vista(request): # la solicitud que recibe del cliente es una request
    return HttpResponse("Ya entendi es muy dificil puta madre !! ") 

def dia_de_hoy(request):
    dia=datetime.datetime.today()
    cadena=f'hoy es {dia}'
    return HttpResponse(cadena)

def saludo_con_nombre(request, nombre):
    return HttpResponse(f'Hola {nombre} como estas?')

def calcula_anio_nacimiento(request, edad):
    anio_actual=datetime.datetime.today().year
    anio_nacimiento=anio_actual-int(edad)
    return HttpResponse(f'<h1>Nacio en el año {anio_nacimiento}</h1>')

""" def probandoHtml(request):
    archivo=open('G:/Mi unidad/coderhouse/MVT/entrega18/proyectoMVT/MVT/platillas/template1.html')

    diccionario={"nombre":"Juan", "apellido": "Perez", "edad":25, "lista_de_notas":[5,4,6,7,8,10,9,7]}

    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario)

    documento=template.render(contexto) # llena mis espacios en blanco con los datos de mi contexto.
    return HttpResponse(documento)"""

def probandoHtml(request):
    
    diccionario={"nombre":"Juan", "apellido": "Perez", "edad":25, "lista_de_notas":[5,4,6,7,8,10,9,7]}
   
    Template= loader.get_template("template1.html") # loader abre archivo lee archivo cierra archivo

    documento=Template.render(diccionario) # llena mis espacios en blanco con los datos de mi contexto.
    return HttpResponse(documento)




