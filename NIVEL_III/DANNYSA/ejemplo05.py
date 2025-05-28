#Importar Librerias
from flask import Flask, request, render_template

#Instancia Flask
app = Flask(__name__)

#Se define ruta para cargar formulario
#Formulario
@app.route('/')
def inicio():
  return render_template('ejemplo05.html')

##@app.route('/',methods=['POST'])
@app.route('/',methods=['POST'])
def procesar_entrada():
  texto_entrada = request.form['entrada']
  texto_procesado = texto_entrada.upper()
  return texto_procesado


if __name__ == '__main__':
  app.run(port=5001)