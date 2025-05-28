# Importación de módulos
from flask import Flask, request, render_template

# Instancia de la clase Flask
app = Flask(__name__)

# Se define la ruta principal para que cargue el
# formulario
@app.route('/')
def inicio():
    return render_template('ejemplo06.html')

@app.route('/', methods=['GET','POST'])
def procesar_entrada():
    if request.method == 'GET':
        texto_entrada = request.args.get('entrada')
        print(texto_entrada)
        texto_entrada_1 = request.form['entrada']
        print(texto_entrada_1)
        if texto_entrada:
            texto_procesado = texto_entrada.upper() # cambia todo el texto a mayúscula
        else: 
            texto_procesado = 'No se ingresó texto'
    return render_template('ejemplo06.html',texto_procesado_plantilla = texto_procesado)

# Ejecutar la aplicación
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla  , port = 5003
    Henry  , port = 5004
    """
    app.run(port=5004)


