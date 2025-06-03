#Importar Librerias
from flask import Flask, request, render_template
import math
#Instancia Flask
app = Flask(__name__)

#Se define ruta para cargar formulario
#Formulario
@app.route('/')
def inicio():
  return render_template('ejemplo09.html')

if __name__ == '__main__':
  app.run(port=5001)
