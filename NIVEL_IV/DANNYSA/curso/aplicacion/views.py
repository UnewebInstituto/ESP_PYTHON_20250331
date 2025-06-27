from django.http import HttpResponse
from django.shortcuts import render

#Modelo
from persona.models import Individuos
from django.db import IntegrityError

def saludo(request):
  return HttpResponse('<h1>Hola estudiantes del curso python django</h1>')

def otrosaludo(request):
  return render(request, 'saludo.html')

def principal(request):
  return render(request, 'index.html')

def persona_ingresar(request):
  return render(request, 'ingresar.html')

def persona_ingresar01(request):
  mensaje=''
  tipo= 0
  if request.method == 'POST':
      try:
        doc = request.POST.get('documento')
        nro = request.POST.get('numero')
        ced = str(doc) + str(nro)
        nom = request.POST.get('nombre')
        ape = request.POST.get('apellido')
        fna = request.POST.get('fechanac')
        ubi = request.POST.get('direccion')
        #Crear instancia de la entidad Individuos en ORM
        individuo = Individuos(cedula=ced, nombre=nom, apellido=ape, fechanac=fna, direccion=ubi)
        #Almacenar registro en ORM
        individuo.save()
        #Emitir mje 
        mensaje = 'Registro almacenado con exito'
        tipo = 1
      except IntegrityError as e:
        mensaje = 'Registro no almacenado por falla de integridad de datos, cedula ya almacenada'
        tipo = 2
      return render(request,'ingresar.html', {'mensaje':mensaje, 'tipo':tipo})
  else:
      mensaje = 'Operacion no permitida'
      tipo = 3 
      return render(request,'ingresar.html', {'mensaje':mensaje, 'tipo':tipo})
  
def persona_reporte(request):
  mensaje = ''
  tipo = '0'
  try:
      datos = Individuos.objects.all
      mensaje = 'Consulta procesada con exito'
      tipo = 1 

  except IntegrityError as e:
     mensaje = 'Fallo la generacion del reporte'
     tipo = 2 
  return render(request, 'reporte.html', {'datos':datos, 'tipo':tipo})
