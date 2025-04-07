SELECT proveedor AS proveedor, max(precio) as maximo_precio,
	min(precio) as mnimo_precio,
	round(avg(precio),2) as	promedio, sum(existencia) as existencia
	FROM public.vista_prov_prod group by proveedor order by proveedor;