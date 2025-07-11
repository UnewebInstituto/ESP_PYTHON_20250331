from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

#Declaración del modelo de datos
from persona.models import Individuos
from django.db import IntegrityError

from datetime import datetime, date

import os
import psycopg2

# Definimos una clase simple para estructurar cada registro de pago móvil (Opcional, pero buena práctica)
# No es estrictamente necesaria si vas a insertar directamente, pero ayuda a la claridad.
# Definimos una clase simple para estructurar cada registro de pago móvil
# Esta clase ayuda a la claridad y a la organización de los datos parseados.
class PagoMovilRegistro:
    def __init__(self, data):
        self.tipo_de_operacion = data.get('tipo_de_operacion')
        self.cod_pagador = data.get('cod_pagador')
        self.id_pagador = data.get('id_pagador')
        self.telf_pagador = data.get('telf_pagador')
        self.cod_receptor = data.get('cod_receptor')
        self.id_receptor = data.get('id_receptor')
        self.telf_receptor = data.get('telf_receptor')
        self.fecha_tx = data.get('fecha_tx')  # Objeto datetime.date
        self.hora_tx = data.get('hora_tx')    # Objeto datetime.time
        self.monto = data.get('monto')        # Flotante
        self.cuenta_pagadora = data.get('cuenta_pagadora')
        self.cuenta_receptora = data.get('cuenta_receptora')
        self.cod_transaccion = data.get('cod_transaccion')
        self.desc_transaccion = data.get('desc_transaccion')
        self.aplicativo = data.get('aplicativo')
        self.canal = data.get('canal')
        self.monto_usd = data.get('monto_usd') # Flotante (calculado si es necesario)
        self.auditoria = data.get('auditoria') # Objeto datetime.date (fecha de carga)

    def __str__(self):
        return (f"Tipo Operación: {self.tipo_de_operacion}, Monto: {self.monto}, "
                f"Fecha: {self.fecha_tx}, Hora: {self.hora_tx}")

# Definición de las posiciones de ancho fijo para cada campo en la línea.
# Estas posiciones se han determinado mediante una inspección cuidadosa del archivo K40L410_250505.TXT.
# Los índices son 0-basados: (inicio_incluido, fin_excluido).
FIELD_SLICES = {
    'banco_pagador_str': (5, 9),          # Ejemplo: '0115'
    'cedula_pagador_full_str': (19, 35),  # Ejemplo: 'V000000006252180' o 'J000...' o vacío
    'telf_pagador_str': (39, 49),         # Ejemplo: '4120223781'
    'banco_receptor_str': (60, 64),       # Ejemplo: '0102'
    'cedula_receptor_full_str': (75, 91), # Ejemplo: '4242451539' o 'J000...' o vacío
    'telf_receptor_str': (96, 106),       # Ejemplo: '109481' o vacío
    'fecha_tx_str': (109, 119),           # Ejemplo: '02-05-2025'
    'hora_tx_str': (122, 130),            # Ejemplo: '22:59:32'
    'trace_str': (133, 139),              # Ejemplo: '267914'
    'auth_str': (142, 148),               # Ejemplo: '109481' o vacío
    'monto_str': (155, 168),              # Ejemplo: '13,00' o '2.000,00'
    'cuenta_pagadora_str': (171, 191),    # Ejemplo: '01150104471005233517' o vacío
    'cuenta_receptora_str': (192, 212),   # Ejemplo: '01150029361005990119' o vacío
    'cod_transaccion_str': (215, 219),    # Ejemplo: '0000' o '0062'
    'desc_transaccion_str': (220, 255),   # Ejemplo: 'LA TARJETA ESTA RESTRINGIDA' o vacío
    'canal_str': (256, 259),              # Ejemplo: 'APP' o 'WEB'
    'cod_ibs_str': (263, 271),            # Ejemplo: '000267914'
}

def parse_line(line):
    """
    Parsea una sola línea del archivo de pagos utilizando posiciones de ancho fijo.
    Retorna un diccionario con los datos parseados y convertidos.
    """
    extracted_data = {}
    for field_name, (start, end) in FIELD_SLICES.items():
        # Asegurarse de que la línea sea lo suficientemente larga para el slice
        if len(line) > end:
            value = line[start:end].strip()
        else:
            value = '' # Asignar cadena vacía si la línea es demasiado corta
        extracted_data[field_name] = value

    # Inicializar el diccionario final con los campos del modelo PagoMovilRegistro
    parsed_record_data = {
        'tipo_de_operacion': extracted_data['banco_pagador_str'],
        'telf_pagador': extracted_data['telf_pagador_str'],
        'cod_receptor': extracted_data['banco_receptor_str'],
        'telf_receptor': extracted_data['telf_receptor_str'],
        'cuenta_pagadora': extracted_data['cuenta_pagadora_str'],
        'cuenta_receptora': extracted_data['cuenta_receptora_str'],
        'cod_transaccion': extracted_data['cod_transaccion_str'],
        'desc_transaccion': extracted_data['desc_transaccion_str'],
        'canal': extracted_data['canal_str'],
        'aplicativo': extracted_data['canal_str'], # Asumiendo que 'aplicativo' es lo mismo que 'canal'
        'monto_usd': None, # Se puede calcular si se tiene una tasa de cambio
        'auditoria': date.today(),
    }

    # Manejo de 'CEDULA PAGADOR' (cod_pagador y id_pagador)
    cedula_pagador_full = extracted_data['cedula_pagador_full_str']
    if len(cedula_pagador_full) > 0 and (cedula_pagador_full[0] in ['V', 'J']):
        parsed_record_data['cod_pagador'] = cedula_pagador_full[0]
        parsed_record_data['id_pagador'] = cedula_pagador_full[1:]
    else:
        parsed_record_data['cod_pagador'] = ''
        parsed_record_data['id_pagador'] = cedula_pagador_full # Si no hay prefijo, es el ID completo

    # Manejo de 'CEDULA RECEPTOR' (id_receptor)
    cedula_receptor_full = extracted_data['cedula_receptor_full_str']
    if len(cedula_receptor_full) > 0 and (cedula_receptor_full[0] in ['V', 'J']):
        parsed_record_data['id_receptor'] = cedula_receptor_full[1:]
    else:
        parsed_record_data['id_receptor'] = cedula_receptor_full # Si no hay prefijo, es el ID completo

    # Conversión de fecha
    try:
        parsed_record_data['fecha_tx'] = datetime.strptime(extracted_data['fecha_tx_str'], '%d-%m-%Y').date()
    except ValueError:
        parsed_record_data['fecha_tx'] = None # O manejar con una fecha por defecto o loguear

    # Conversión de hora
    try:
        parsed_record_data['hora_tx'] = datetime.strptime(extracted_data['hora_tx_str'], '%H:%M:%S').time()
    except ValueError:
        parsed_record_data['hora_tx'] = None # O manejar con una hora por defecto o loguear

    # Conversión de monto (maneja miles con punto y decimales con coma)
    try:
        monto_str_cleaned = extracted_data['monto_str'].replace('.', '').replace(',', '.')
        parsed_record_data['monto'] = float(monto_str_cleaned)
    except ValueError:
        parsed_record_data['monto'] = 0.0 # Valor por defecto en caso de error de conversión

    return parsed_record_data


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

def persona_actualizar01(request):
    mensaje = ""
    tipo = 0
    nom = ""
    ape = ""
    cor = ""
    fna = ""
    ubi = ""
    if request.method == 'GET':
        try:
            id_tmp = request.GET.get('id')
            # Se consulta mediante la cedula usando el ORM
            individuo = Individuos.objects.get(id = id_tmp)
            # Se extraen los campos del registro
            ced = individuo.cedula
            nom = individuo.nombre
            ape = individuo.apellido
            fna = individuo.fechanac
            print("TIPO CAMPO fna:" , type(fna))
            print("FECHA DE NACIMIENTO:" , str(fna))
            fna = fna.strftime('%Y-%m-%d')
            print("FECHA DE NACIMIENTO FORMATEADA:",fna)
            ubi = individuo.direccion
            # Se prepara la salida
            tipo = 1
            mensaje = "Consulta procesada con éxito."
            return render(request, "actualizar01.html", {"mensaje":mensaje, "tipo":tipo, "cedula":ced,  "nombre": nom, "apellido":ape, "fechanac":fna, "direccion":ubi, "id":id_tmp})
        except Individuos.DoesNotExist:
            tipo = 2
            mensaje = "Registro no encontrado."
            return render(request, "actualizar01.html", {"mensaje":mensaje, "tipo": tipo})

def persona_actualizar02(request):
    mensaje = ''
    tipo = 0
    if request.method == 'POST':
        try:
            # Extracción de datos del formulario
            id_tmp = request.POST.get('id')
            nom = request.POST.get('nombre')
            ape = request.POST.get('apellido')
            fna = request.POST.get('fechanac')
            ubi = request.POST.get('direccion')
            # Crear instancia de la entidad Individuos en el ORM
            Individuos.objects.filter(id=id_tmp).update(nombre=nom, apellido=ape, fechanac=fna, direccion=ubi)
            # Emitir mensaje de aprobación
            mensaje = 'Regitro actualizado con éxito.'
            tipo = 1
        except IntegrityError as e:
            mensaje = 'Registro no fue actualizado, por falla de integridad de datos.'
            tipo = 2
        datos = Individuos.objects.all()
        return render(request, 'actualizar.html', {'datos':datos, 'tipo':tipo, 'mensaje':mensaje})
    else:
        mensaje = 'Operación no permitida.'
        tipo = 3
        return render(request, 'ingresar.html', {'mensaje':mensaje, 'tipo':tipo})

def ejemplo01_js(request):
    return render(request, 'ejemplo01_js.html')

def ejemplo02_js(request):
    return render(request, 'ejemplo02_js.html')

def ejemplo03_js(request):
    
    return render(request, 'ejemplo03_js.html')

def ejemplo01_jq(request):
    return render(request, 'ejemplo01_jq.html')

def ejemplo02_jq(request):
    return render(request, 'ejemplo02_jq.html')

def ejemplo03_jq(request):
    return render(request, 'ejemplo03_jq.html')

def persona_api_json(request):
    mensaje = ''
    tipo = 0
    try:
        datos = list(Individuos.objects.values())
        mensaje = 'Consulta a la Api en formato JSON, procesada con éxito'
        tipo = 1
        response_data = {
            'tipo': tipo,
            'mensaje': mensaje,
            'datos': datos
        }
        return JsonResponse(response_data)
    except Exception as e:
        mensaje = 'Ocurrio un error al ejecutar la Api en formato JSON'
        tipo = 2
        response_data = {
            'tipo': tipo,
            'mensaje': mensaje
        }
        return JsonResponse(response_data, status=500)


def persona_reporte_api_json(request):
    return render(request, 'persona_reporte_api_json.html')


def persona_exportar_excel(request):
    #formato del nombre de archivo: persona_aaaammdd_hhmmss.csv
    import psycopg2
    import pandas as pd
    from datetime import datetime
    import os

    # --- Configuración de la base de datos ---
    DB_HOST = "localhost"
    DB_NAME = "bd_nivel2_carla"
    DB_USER = "postgres"  # <--- CAMBIA ESTO por tu usuario de PostgreSQL
    DB_PASSWORD = "123456" # <--- CAMBIA ESTO por tu contraseña de PostgreSQL
    DB_PORT = "5432"

    # --- Configuración de la exportación ---
    EXPORT_DIR = r"C:\ESP_PYTHON_20250331\NIVEL_V\CARLA\excel" # La 'r' es para raw string, evita problemas con barras invertidas
    TABLE_NAME = "persona_individuos"
    OUTPUT_FILENAME_BASE = "persona_individuos"
    """
    Exporta la tabla persona_individuos de PostgreSQL a un archivo Excel (.xlsx)
    con un nombre de archivo dinámico basado en la fecha y hora.
    """
    try:
        # Crea la ruta de exportación si no existe
        os.makedirs(EXPORT_DIR, exist_ok=True)

        # Genera el nombre del archivo con la fecha y hora actuales
        current_datetime = datetime.now()
        timestamp = current_datetime.strftime("%Y%m%d_%H%M%S")
        output_filename = f"{OUTPUT_FILENAME_BASE}_{timestamp}.xlsx"
        output_filepath = os.path.join(EXPORT_DIR, output_filename)

        print(f"Conectándose a la base de datos '{DB_NAME}'...")
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Conexión exitosa.")

        # Consulta para seleccionar todos los datos de la tabla
        query = f"SELECT id, cedula, nombre, apellido, direccion, fechanac FROM {TABLE_NAME};"

        print(f"Cargando datos de la tabla '{TABLE_NAME}'...")
        # Usa pandas para leer los datos directamente de PostgreSQL
        df = pd.read_sql_query(query, conn)
        print(f"Datos cargados. Filas: {len(df)}")

        # Guarda el DataFrame en un archivo Excel
        print(f"Exportando datos a: {output_filepath}")
        df.to_excel(output_filepath, index=False) # index=False para no escribir el índice de pandas
        print("Exportación a Excel completada exitosamente.")
        tipo = 1
        mensaje = "Exportación a Excel completada exitosamente."
    except psycopg2.Error as e:
        print(f"Error de base de datos: {e}")
        tipo = 2
        mensaje = "Error de base de datos"
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        tipo = 3
        mensaje = "ocurrio un error"
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Conexión a la base de datos cerrada.")
    return render(request, 'index.html', {'mensaje':mensaje, 'tipo':tipo})

def importar_pago_movil(request):
    """
    Lee un archivo plano de pagos móviles, parsea cada registro
    y lo inserta en la tabla `pago_movil` de PostgreSQL.
    """
    # Ruta del archivo (manteniendo la ruta proporcionada por el usuario)
    file_path = 'C:/ESP_PYTHON_20250331/NIVEL_II/data/K40L410_250505.TXT'
    num_registros_insertados = 0
    mensaje = ''
    tipo = 1 # Tipo 1 para éxito, 2 para error (para la plantilla HTML)
    conn = None # Inicializa la conexión a None

    # --- Configuración de la base de datos ---
    # Asegúrate de que estos valores sean correctos para tu entorno PostgreSQL
    DB_HOST = "localhost"
    DB_NAME = "bd_nivel2_carla"
    DB_USER = "postgres"  # <--- CAMBIA ESTO por tu usuario de PostgreSQL
    DB_PASSWORD = "123456" # <--- CAMBIA ESTO por tu contraseña de PostgreSQL
    DB_PORT = "5432"

    try:
        # Verificar si el archivo existe
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo no se encontró en la ruta: {file_path}")

        print(f"Conectándose a la base de datos '{DB_NAME}'...")
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        # Habilitar autocommit: cada sentencia SQL (INSERT) se confirmará automáticamente.
        # Esto previene el estado de "transacción abortada" si una inserción falla,
        # permitiendo que el resto de las inserciones continúen.
        conn.autocommit = True
        print("Conexión exitosa. Iniciando lectura y procesamiento del archivo...")

        # --- TRUNCAR LA TABLA ANTES DE LA INSERCIÓN ---
        with conn.cursor() as cur:
            print(f"Truncando la tabla 'pago_movil' en la base de datos '{DB_NAME}'...")
            cur.execute("TRUNCATE TABLE pago_movil;")
            # No es necesario conn.commit() después de TRUNCATE si autocommit es True
            print("Tabla 'pago_movil' truncada exitosamente.")

        # Leer todas las líneas del archivo
        with open(file_path, 'r', encoding='utf-8') as pago_movil_file:
            lista_registros_raw = pago_movil_file.readlines()

        print(f"Se encontraron {len(lista_registros_raw)} líneas en el archivo.")

        # Las primeras 6 líneas son cabeceras que deben ser ignoradas.
        # Las últimas líneas son resúmenes que también deben ser ignoradas.
        # Se asume que las líneas de datos comienzan en la línea 7 (índice 6).
        # Se filtran las líneas de pie de página por su contenido.
        data_lines = []
        skip_footer = False
        for line in lista_registros_raw[6:]: # Empezar desde el índice 6 (línea 7)
            stripped_line = line.strip()
            if stripped_line.startswith('TOTAL GENERAL') or \
               stripped_line.startswith('TRANSACCIONES PROCESADAS') or \
               stripped_line.startswith('TRANSACCIONES ACEPTADAS') or \
               stripped_line == '': # También ignorar líneas completamente vacías en el cuerpo del archivo
                skip_footer = True
                continue
            if not skip_footer:
                data_lines.append(line) # Añadir la línea original para el slicing

        print(f"Procesando {len(data_lines)} registros de datos válidos...")

        with conn.cursor() as cur: # Usar un cursor para ejecutar comandos SQL
            for i, registro_raw in enumerate(data_lines):
                # Usar la línea original (no stripped) para el parseo de ancho fijo
                # ya que los espacios iniciales son parte de la estructura fija.
                # Se limpia el strip() solo para el mensaje de log si es necesario.
                registro_limpio_para_log = registro_raw.strip()

                try:
                    parsed_data = parse_line(registro_raw) # Pasar la línea cruda para el slicing

                    # Construcción de la consulta SQL para INSERT
                    insert_query = """
                    INSERT INTO pago_movil (
                        tipo_de_operacion, cod_pagador, id_pagador, telf_pagador,
                        cod_receptor, id_receptor, telf_receptor, fecha_tx, hora_tx,
                        monto, cuenta_pagadora, cuenta_receptora, cod_transaccion,
                        desc_transaccion, aplicativo, canal, monto_usd, auditoria
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    );
                    """
                    # Tupla de valores a insertar, en el mismo orden que las columnas en INSERT INTO
                    values = (
                        parsed_data['tipo_de_operacion'],
                        parsed_data['cod_pagador'],
                        parsed_data['id_pagador'],
                        parsed_data['telf_pagador'],
                        parsed_data['cod_receptor'],
                        parsed_data['id_receptor'],
                        parsed_data['telf_receptor'],
                        parsed_data['fecha_tx'],
                        parsed_data['hora_tx'],
                        parsed_data['monto'],
                        parsed_data['cuenta_pagadora'],
                        parsed_data['cuenta_receptora'],
                        parsed_data['cod_transaccion'],
                        parsed_data['desc_transaccion'],
                        parsed_data['aplicativo'],
                        parsed_data['canal'],
                        parsed_data['monto_usd'],
                        parsed_data['auditoria']
                    )

                    # Ejecutar la inserción
                    cur.execute(insert_query, values)
                    num_registros_insertados += 1

                except (ValueError, IndexError, psycopg2.Error) as e:
                    # Captura errores de parseo (ValueError, IndexError) y de DB (psycopg2.Error)
                    print(f"Error procesando/insertando registro {i+1} ('{registro_limpio_para_log}'): {e}")
                    # Con autocommit=True, no se necesita rollback aquí para cada error de sentencia.
                    # La transacción para esta sentencia ya falló y fue manejada.
                    continue # Saltar al siguiente registro si hay un error

        mensaje = f"Carga de datos completada. Se insertaron {num_registros_insertados} registros en la tabla 'pago_movil'."
        print(mensaje)

    except FileNotFoundError as e:
        mensaje = f"Error: {e}"
        tipo = 2
        print(mensaje)
    except psycopg2.Error as e:
        # Este bloque captura errores de conexión a la base de datos o errores globales.
        mensaje = f"Error de base de datos durante la conexión o el procesamiento: {e}"
        tipo = 2
        print(mensaje)
        # Si la conexión no está en autocommit (aunque la habilitamos), un rollback es buena práctica
        # para asegurar que no queden transacciones pendientes en caso de errores de conexión.
        if conn and not conn.autocommit:
            conn.rollback()
    except Exception as e:
        # Captura cualquier otro error inesperado
        mensaje = f"Ocurrió un error inesperado: {e}"
        tipo = 2
        print(mensaje)
    finally:
        # Cerrar la conexión a la base de datos si se estableció
        if conn:
            conn.close()
            print("Conexión a la base de datos cerrada.")

    # Renderizar la plantilla HTML con el mensaje de resultado
    return render(request, 'index.html', {'mensaje':mensaje, 'tipo':tipo})