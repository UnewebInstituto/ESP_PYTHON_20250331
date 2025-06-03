# Importación de módulos
from flask import Flask, request, render_template
import math

# Instancia de la clase Flask
app = Flask(__name__)

# Se define la ruta principal para que cargue el
# formulario
@app.route('/')
def inicio():
    return render_template('ejemplo09.html')


# Ejecutar la aplicación
if __name__ == '__main__':
    """
    Dannysa, port = 5001
    Orlanys, port = 5002
    Carla  , port = 5003
    Henry  , port = 5004
    """
    app.run(port=5003)