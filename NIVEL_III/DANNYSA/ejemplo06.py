#Importar Librerias
from flask import Flask, request, render_template

#Instancia Flask
app = Flask(__name__)

#Se define ruta para cargar formulario
#Formulario
@app.route('/')
def inicio():
  return render_template('ejemplo06.html')

@app.route('/',methods=['GET','POST'])
def procesar_entrada():
    if request.method == 'GET':
        texto_entrada = request.args.get('entrada')
        if texto_entrada:
          texto_procesado = texto_entrada.upper()
        else:
          texto_procesado = 'No se ingreso texto'
    return render_template('ejemplo06.html', texto_procesado_plantilla = texto_procesado)


if __name__ == '__main__':
  app.run(port=5001)