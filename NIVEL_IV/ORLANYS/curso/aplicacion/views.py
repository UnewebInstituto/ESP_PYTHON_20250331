from django.http import HttpResponse
from django.shortcuts import render

#Declaración del modelo de datos
from persona.models import Individuos
from django.db import IntegrityError

def saludo(request):
    return HttpResponse("<h1>Hola estudiantes del curso de Python Django</h1>")

def otrosaludo(request):
    return render(request, 'saludo.html')

def principal(request):
    return render(request, 'index.html')

def persona_ingresar(request):
    return render(request, 'ingresar.html')

def persona_ingresar01(request):
    mensaje = ''
    tipo = 0
    if request.method == 'POST':
        try:
            # Extracción de datos del formulario
            doc = request.POST.get('documento')
            nro = request.POST.get('numero')
            ced = str(doc) + str(nro)
            nom = request.POST.get('nombre')
            ape = request.POST.get('apellido')
            fna = request.POST.get('fechanac')
            ubi = request.POST.get('direccion')
            # Crear instancia de la entidad Individuos en el ORM
            individuo = Individuos(cedula=ced, nombre=nom, apellido=ape, fechanac=fna, direccion=ubi)
            # Almacenar registro a través del ORM
            individuo.save()
            # Emitir mensaje de aprobación
            mensaje = 'Regitro almacenado con éxito.'
            tipo = 1
        except IntegrityError as e:
            mensaje = 'Registro no fue almacenado, por falla de integridad de datos. Cédula ya existe.'
            tipo = 2
        return render(request, 'ingresar.html', {'mensaje':mensaje, 'tipo':tipo})
    else:
        mensaje = 'Operación no permitida.'
        tipo = 3
        return render(request, 'ingresar.html', {'mensaje':mensaje, 'tipo':tipo})

def persona_reporte(request):
    mensaje = ''
    tipo = 0
    try:
        datos = Individuos.objects.all()
        mensaje = 'Consulta procesada con éxito.'
        tipo = 1
    except IntegrityError as e:
        mensaje = 'Falló la generación del reporte.'
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
        # Se concatena doccumento y número
        ced = doc + nro
        # Se consulta mediante la cedula usando el ORM
        individuo = Individuos.objects.get(cedula = ced)
        # Se extraen los campos del registro
        nom = individuo.nombre
        ape = individuo.apellido
        fna = individuo.fechanac
        ubi = individuo.direccion
        # Se prepara la salida
        tipo = 1
        mensaje = "Consulta procesada con éxito."
        return render(request, "consultar01.html", {"mensaje":mensaje, "tipo":tipo, "cedula":ced,  "nombre": nom, "apellido":ape, "fechanac":fna, "direccion":ubi})
    except Individuos.DoesNotExist:
        tipo = 2
        mensaje = "Cédula de identidad no encontrada."
        return render(request, "consultar01.html", {"mensaje":mensaje, "tipo": tipo})


def persona_borrar(request):
    mensaje = ''
    tipo = 0
    try:
        datos = Individuos.objects.all()
        mensaje = 'Consulta procesada con éxito.'
        tipo = 1
    except IntegrityError as e:
        mensaje = 'Falló la generación del reporte.'
        tipo = 2
    return render(request, 'borrar.html', {'datos':datos, 'tipo':tipo})

def persona_borrar01(request):
    mensaje = ''
    tipo = 0
    if request.method == 'GET':
        try:
            id_tmp = request.GET.get('id')
            Individuos.objects.filter(id=id_tmp).delete()
            mensaje = 'El registro fue borrado con éxito'
            tipo = 1
        except Exception as e:
            mensaje = 'Ocurrio un error al intentar borrar el registro' + str(e)
            tipo = 2
        datos = Individuos.objects.all()
        return render(request,'borrar.html',{'mensaje':mensaje, 'tipo':tipo, 'datos':datos})


def persona_actualizar(request):
    mensaje = ''
    tipo = 0
    try:
        datos = Individuos.objects.all()
        mensaje = 'Consulta procesada con éxito.'
        tipo = 1
    except IntegrityError as e:
        mensaje = 'Falló la generación del reporte.'
        tipo = 2
    return render(request, 'actualizar.html', {'datos':datos, 'tipo':tipo})

    



