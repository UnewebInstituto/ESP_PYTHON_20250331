from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
  return HttpResponse("<h1>Hola estudiantes del curso de Python Django</h1>")

  def otrosaludo(request):
    return render(request, 'saludo.html')