input_file = 'C:/ESP_PYTHON_20250331/NIVEL_II/data/K40L410_250505.txt'
output_file = 'C:/ESP_PYTHON_20250331/NIVEL_II/carla/K40L410_250505_clean.txt'
registro_longitud = 267

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    buffer = ''
    for line in infile:
        buffer += line.rstrip('\n\r')
        while len(buffer) >= registro_longitud:
            registro = buffer[:registro_longitud]
            outfile.write(registro + '\n')
            buffer = buffer[registro_longitud:]
    # Si queda basura en buffer, puedes decidir si la ignoras o la reportas
    if buffer:
        print("Registro incompleto al final del archivo:", repr(buffer))