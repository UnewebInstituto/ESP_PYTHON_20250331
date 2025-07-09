from django.db import models

# Create your models here.

class Individuos(models.Model):
    # Declaración de campos en la tabla
    cedula = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.TextField()
    fechanac = models.DateField()
    # Definición de método que permita acceder a los valores
    # contenidos en la tabla a través del ORM

    def __str__(self):
        return '%s %s %s %s %s %s'%(self.id, self.cedula, self.nombre, self.apellido, self.direccion, self.fechanac)



