SELECT proveedor AS "Proveedor", max(precio) as "Màximo precio",
	min(precio) as "Mìnimo precio",
	round(avg(precio),2) as	"Promedio", sum(existencia) as "Existencia"
	FROM public.vista_prov_prod group by proveedor order by proveedor;