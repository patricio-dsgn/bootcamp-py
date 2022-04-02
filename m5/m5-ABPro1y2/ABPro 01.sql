#SELECT NombreVendedor as 'vendedor', salario as "Salario > al Promedio" FROM vendedor WHERE salario > (SELECT AVG(salario) FROM vendedor)
#SELECT NombreProducto as 'Producto', Precio as "precio > al Promedio" FROM productos WHERE Precio > (SELECT AVG(Precio) FROM productos)
#SELECT Nombre as 'Cliente', TotalPagado as "Pagado > al Promedio" FROM clientes WHERE TotalPagado > (SELECT AVG(TotalPagado) FROM clientes)
#COUNT(NombreVendedor) as 'vendedor' FROM vendedor WHERE salario < (SELECT AVG(salario) FROM vendedor)
#SELECT COUNT(NombreProducto) as 'N° Productos' FROM productos WHERE Precio < (SELECT AVG(Precio) FROM productos)
#SELECT NombreVendedor as 'Nombre', ApellidosVendedor as 'Apellido', salario as "Salario > al Promedio" FROM vendedor WHERE salario > (SELECT AVG(salario) FROM vendedor)
#(SELECT NombreProducto as 'Producto', Precio  from productos order by Precio desc limit 1) union
#(SELECT NombreProducto , Precio from productos order by Precio asc limit 1)
#SELECT SUM(Precio) as 'Costo Total' from productos

#SELECT   Comuna ,   COUNT(Comuna ) AS `Más Clientes x Comuna`
#FROM   clientes GROUP BY   Comuna
#ORDER BY    `Más Clientes x Comuna`  DESC LIMIT 1

SELECT NombreProducto as 'Producto',  Stock as "Stock > 5" FROM productos WHERE Stock > 5 #(SELECT AVG(Precio) FROM productos)

