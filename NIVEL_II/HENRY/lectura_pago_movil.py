pago_movil = open('C:/ESP_PYTHON_20250331/NIVEL_II/data/K40L410_250505.TXT')

lista_pago_movil = pago_movil.readlines()

for registro in lista_pago_movil:
    """
    cod_pagador = registro[5:9]
    id_pagador = registro[15:32]
    if id_pagador[0] in ('V','E','J'): 
        print(cod_pagador, id_pagador)
    """
    print(registro[5:9], registro[15:32])

