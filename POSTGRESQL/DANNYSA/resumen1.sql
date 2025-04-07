SELECT proveedor AS proveedor,
	max(precio) as Maximo_Precio,
	min(precio) as Minimo_precio,
	ROUND(avg(precio),2) as Promedio,
	sum(existencia) as Existencia
	FROM public."VISTA_PROV_PROD"
    group by proveedor
	order by proveedor;