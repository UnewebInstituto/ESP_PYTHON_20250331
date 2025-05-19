\c bd_nivel2_carla

create table pago_movil(
    c1 varchar(5),
    cod_pagador varchar(4),
    c2 varchar(6),
    id_pagador varchar(16),
    c3 varchar(236)
);

-- copia de un archivo plano a una tabla de base de datos
-- El archivo es de longitud variable, por tanto 
-- hay que colocar delimitadores para llevarlo a
-- formato csv
--COPY pago_movil FROM 'C:/ESP_PYTHON_20250331/NIVEL_II/data/K40L410_250505.txt';

copy pago_movil FROM 'C:/ESP_PYTHON_20250331/NIVEL_II/CARLA/K40L410_250505.csv' WITH (FORMAT csv);

-- 2da. Forma

CREATE TEMP TABLE temp_pagos(linea TEXT);
COPY temp_pagos FROM 'C:/ESP_PYTHON_20250331/NIVEL_II/data/K40L410_250505.txt';

COPY temp_pagos FROM 'C:/ESP_PYTHON_20250331/NIVEL_II/CARLA/K40L410_250505;

INSERT INTO pago_movil
SELECT
    SUBSTRING(linea FROM 1 FOR 5) AS c1,
    SUBSTRING(linea FROM 6 FOR 4) AS cod_pagador,
    SUBSTRING(linea FROM 10 FOR 6) AS c2,
    SUBSTRING(linea FROM 16 FOR 16) AS id_pagador,
    SUBSTRING(linea FROM 32 FOR 236) AS c3
FROM temp_pagos;

