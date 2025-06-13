CREATE TABLE pago_movil
(
    tipo_de_operacion text,
    cod_pagador character varying(20),
    id_pagador character varying(20),
    telf_pagador character(10),
    cod_receptor character varying(20),
    id_receptor character varying(20),
    telf_receptor character(10),
    fecha_tx date,
    hora_tx time without time zone,
    monto numeric(10,2),
    cuenta_pagadora character varying(30),
    cuenta_receptora character varying(30),
    cod_transaccion character varying(20),
    desc_transaccion text,
    aplicativo text,
    canal text,
    monto_usd numeric(10,2),
    auditoria date
);