from django.db import models


# Create your models here. # ESTOS SON LOS MODELOS TABLAS DE BASE DE DATOS los objetos se crean en un views
class Papa(models.Model): # es una herencia objeto
    
    nombre=models.CharField(max_length=20) # campo de texto
    apellido=models.CharField(max_length=20)
    nacimiento=models.CharField(max_length=20)
    edad=models.IntegerField() # numeros enteros
   

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+self.nacimiento

class Madre(models.Model): # es una herencia objeto
    
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    nacimiento=models.CharField(max_length=20)
    edad=models.IntegerField()
    
    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+self.nacimiento

class Hermana(models.Model): # es una herencia objeto
    
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    nacimiento=models.CharField(max_length=20)
    edad=models.IntegerField()
    

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+self.nacimiento