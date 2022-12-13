from django.db import models

# Create your models here. clase curso

class Curso(models.Model):
    nombre=models.CharField(max_length=50) # es el str
    comision=models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.comision)