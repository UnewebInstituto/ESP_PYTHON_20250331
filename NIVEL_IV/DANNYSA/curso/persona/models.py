from django.db import models

# Create your models here.
class Individuos(models.Model):
  cedula = models.CharField(max_length=10, unique=True)
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  direccion = models.TextField()
  fechanac = models.DateField()

  #def de metodos para acceder a los valores en la tabla a traves de ORN

  def __str__(self):
    return '%s %s %s %s %s %s'%(self.id, self.cedula, self.nombre, self.apellido, self.direccion, self.fechanac) 



