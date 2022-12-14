from django.db import models

# Create your models here. clase curso

class Familiares(models.Model):
    nombre=models.CharField(max_length=20) # es el str
    tipoFamilia=models.IntegerField()
    edad=models.IntegerField(max_length=2)

    def __str__(self):
        return self.nombre+" "+str(self.tipoFamilia)+" "+str(self.edad)