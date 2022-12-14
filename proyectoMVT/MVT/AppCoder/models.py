from django.db import models

# Create your models here.
class Papa(models.Model): # es una herencia objeto
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    nacimiento=models.DateField()
    edad=models.BooleanField()
    profesion=models.CharField(max_length=20)

class Mama(models.Model): # es una herencia objeto
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    nacimiento=models.DateField()
    edad=models.BooleanField()
    profesion=models.CharField(max_length=20)

class Hermana(models.Model): # es una herencia objeto
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    nacimiento=models.DateField()
    edad=models.BooleanField()
    profesion=models.CharField(max_length=20)
