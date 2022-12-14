from django.db import models

# Create your models here.
class Papa(models.Model): # es una herencia objeto
    
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    nacimiento=models.DateField()
    edad=models.IntegerField()
    profesion=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+self.nacimiento+" "+self.profesion

class Mama(models.Model): # es una herencia objeto
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    nacimiento=models.DateField()
    edad=models.IntegerField()
    profesion=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+self.nacimiento+" "+self.profesion

class Hermana(models.Model): # es una herencia objeto
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    nacimiento=models.DateField()
    edad=models.IntegerField()
    profesion=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+self.nacimiento+" "+self.profesion