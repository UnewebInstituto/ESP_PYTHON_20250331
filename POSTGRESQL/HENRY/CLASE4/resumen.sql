SELECT proveedor as "Proveedor", max(precio) as "Máximo precio", 
	min(precio) as "Mínimo precio", 
	round(avg(precio),2) as "Promedio",
	sum(existencia) as "Existencia"
	FROM public.vista_prov_prod group by proveedor order by proveedor;