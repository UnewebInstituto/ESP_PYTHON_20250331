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
def persona_consultar(request):
  return render(request, 'consultar.html')
def persona_consultar01(request):
  mensaje = ""
  tipo = 0
  nom = ""
  ape = ""
  cor = ""
  fna = ""
  ubi = ""
  try:
    doc = request.POST.get("documento")
    nro = request.POST.get("numero")
    ced = doc + nro
    individuo = Individuos.objects.get(cedula = ced)
    nom = individuo.nombre
    ape = individuo.apellido
    fna = individuo.fechanac
    ubi = individuo.direccion 

    tipo = 1
    mensaje = "Consulta procesada con exito"
    return render(request, "consultar01.html", {"mensaje":mensaje, "tipo": tipo, "cedula": ced, "nombre": nom, "apellido": ape, "fechanac": fna, "direccion": ubi})
  except Individuos.DoesNotExist:
    tipo = 2
    mensaje = "Cedula de identidad no encontrada"
    return render(request, "consultar01.html", {"mensaje":mensaje, "tipo": tipo}) 
  
def persona_borrar(request):
    mensaje = ''
    tipo = '0'
    try:
        datos = Individuos.objects.all
        mensaje = 'Consulta procesada con exito'
        tipo = 1 

    except IntegrityError as e:
      mensaje = 'Fallo la generacion del reporte'
      tipo = 2 
    return render(request, 'borrar.html', {'datos':datos, 'tipo':tipo})

def persona_borrar01(request):
    mensaje =''
    tipo = 0
    if request.method == 'GET':
      try:
          id_temp = request.GET.get('id')
          Individuos.objects.filter(id= id_temp).delete()
          mensaje = 'Registro borrado con exito'
          tipo = 1
      except Exception as e:
         mensaje = 'Ocurrio un error al intentar borrar registro' + str(e)
         tipo = 2
      datos = Individuos.objects.all()
      return render(request, 'borrar.html', {'mensaje':mensaje, 'tipo':tipo, 'datos':datos})
def persona_actualizar(request):
    mensaje = ''
    tipo = '0'
    try:
        datos = Individuos.objects.all
        mensaje = 'Consulta procesada con exito'
        tipo = 1 

    except IntegrityError as e:
      mensaje = 'Fallo la generacion del reporte'
      tipo = 2 
    return render(request, 'actualizar.html', {'datos':datos, 'tipo':tipo})
