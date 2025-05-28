#Importar Librerias
from flask import Flask, request, render_template
import math
#Instancia Flask
app = Flask(__name__)

#Se define ruta para cargar formulario
#Formulario
@app.route('/')
def inicio():
  return render_template('ejemplo07.html')

@app.route('/',methods=['GET','POST'])
def procesar_entrada():
    if request.method == 'POST':
       a = eval(request.form['a'])
       b = eval(request.form['b'])
       c = eval(request.form['c'])
       if a == 0:
          texto_resultado = 'Error: valor de a debe ser diferente de cero'
       else:
          sub_radical = b*b - 4*a*c
          if sub_radical < 0:
             texto_resultado = 'Error: valor de expresion sub radical no debe ser negativa'
          else:
             x1 = (-b+math.sqrt(sub_radical))/(2*a)
             x2 = (-b-math.sqrt(sub_radical))/(2*a)
             texto_resultado = 'x1=' + str(x1) +',x2=' + str(x2)

       return render_template('ejemplo07.html', resultado = texto_resultado)

if __name__ == '__main__':
  app.run(port=5001)
