from django.db import models

# Create your models here. clase curso

class Padre(models.Model):
    papa=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20) # es el str #campo de texto caracteres
    apellido=models.CharField(max_length=20)
    edad=models.IntegerField()
    profesion=models.CharField()

    def __str__(self):
        return self.nombre+" "+(self.apellido)+" "+str(self.edad)

class Mama(models.Model):
    mama=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20) # es el str
    apellido=models.CharField(max_length=20)
    edad=models.IntegerField()    
    profesion=models.CharField()

class Hermana(models.Model):
    hermana=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20) # es el str
    apellido=models.CharField(max_length=20)
    edad=models.IntegerField()
    profesion=models.CharField()