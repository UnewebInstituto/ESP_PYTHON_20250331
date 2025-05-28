# Importaciòn de mòdulos
from flask import Flask, request, render_template

# Instancia de clase Flask
app = Flask(__name__)

# Se define la ruta principal para que cargue el formulario
@app.route('/')
def inicio():
    return render_template('ejemplo05.html')


# @app.route('/',methods=['POST'])
def procesar_entrada():
    texto_entrada = request.form['entrada']
    texto_procesado = texto_entrada.upper()
    # Cambia todo el texto a mayùscula
    return texto_procesado

# Ejecutar la aplicaciòn
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla, port = 5003
    Henry, port = 5004
    """

    app.run(port=5002)

