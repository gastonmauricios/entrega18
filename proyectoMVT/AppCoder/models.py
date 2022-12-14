from django.db import models

# Create your models here. clase curso

class Padre(models.Model):
    papa=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20) # es el str #campo de texto caracteres
    apellido=models.CharField(max_length=20)
    naciemiento=models.DateField()   
    edad=models.BooleanField()

    def __str__(self):
        return self.nombre+" "+(self.apellido)+" "+str(self.edad)+" "+str(self.papa)

class Mama(models.Model):
    mama=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20) # es el str
    apellido=models.CharField(max_length=20)
    naciemiento=models.DateField()    
    edad=models.BooleanField()

class Hermana(models.Model):
    hermana=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20) # es el str
    apellido=models.CharField(max_length=20)
    naciemiento=models.DateField()   
    edad=models.BooleanField()