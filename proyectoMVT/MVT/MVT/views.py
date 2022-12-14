from django.http import HttpResponse

def saludar(request):
    return HttpResponse("hola mundo") #todo proyecto en django se comunica con el user a travez solicitud y recibe respuestas.