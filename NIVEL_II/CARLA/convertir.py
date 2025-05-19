input_file = 'C:/ESP_PYTHON_20250331/NIVEL_II/data/K40L410_250505.txt'
output_file = 'C:/ESP_PYTHON_20250331/NIVEL_II/CARLA/K40L410_250505.csv'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        c1 = line[0:5].strip()
        cod_pagador = line[5:9].strip()
        c2 = line[9:15].strip()
        id_pagador = line[15:31].strip()
        c3 = line[31:267].strip()
        outfile.write(f'{c1},{cod_pagador},{c2},{id_pagador},{c3}\n')