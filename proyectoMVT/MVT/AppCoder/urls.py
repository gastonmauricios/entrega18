
from django.urls import path
from .views import * # un punto . es un directorios .. dos directorio

urlpatterns = [
    
    
    path('papa/', papa),
    path('mama/', mama),
    path('hermana/', hermana),
   
    
]