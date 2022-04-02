INSERT INTO productos(SKU, NombreProducto, Categoria, Fabricante, Stock, Precio)
values (1001,'Parlantes','electronica','Jbl',15,10000),
(1002,'Notebook','computacion','HP',89,800000),
(1003,'PC Gamer','computacion','Asus',20,1500000),
(1004,'Swicht','computacion','Nintendo',60,350000),
(1005,'Microondas','Linea Blana','Ursus Trotter',100,400000),
(1006,'Teclado','Musica','Casio',32,150000),
(1007,'Tijeras Poda','Jardin','Fitting',75,20000),
(1008,'Living para Terraza','Terraza','Ikea',81,300000),
(1009,'Cocina','Linea Blana','Madensa',4,200000),
(1010,'Polera','Ropa Mujer','Zara',52,50000);



INSERT INTO clientes(idclientes, Nombre, Apellido, Telefono, Dirección, Comuna, Email, FechaRegistro, TotalPagado)
VALUES (17485284,'Jose','Balmaceda','909605427','peragallo 99','Valparaiso','Jose@gmail.com','1967-07-02',491616),
(5857694,'Manule','Campor','946446674','viana1255','Viña ','Manule@gmail.com','1964-03-03',340336),
(15966257,'Isaac','Benavides','964925545','alvarez 55','Quillota','Isaac@gmail.com','1964-03-03',49235),
(18784266,'Lorena','Morales','926899982','1 norte 580','Quilpue','Lorena@gmail.com','1964-03-03',383224),
(6569192,'Jorge','Castro','959151737','limache 3405','Villa alemana','Jorge@gmail.com','1964-03-03',342375),
(15608269,'Claudio','Silva','928374756','peragallo 99','Viña ','Claudio@gmail.com','1964-03-03',362221),
(13902911,'Alonso','Jaramillo','965226693','viana1255','Quillota','Alonso@gmail.com','1964-03-03',76054),
(9921931,'Miguel','Tapia','986797404','alvarez 55','Quilpue','Miguel@gmail.com','1964-03-03',175199),
(15640021,'Pedro','Pascal','961240792','1 norte 580','Villa alemana','Pedro@gmail.com','1964-03-03',365128),
(12289693,'Luis','Jara ','941998957','limache 3405','Viña ','Luis@gmail.com','1964-03-03',371133);

INSERT INTO vendedor(Run, NombreVendedor, ApellidosVendedor, FechaNacimiento, Sección) 
VALUES 
(7598753, 'Pedro', 'Paramo', '1988-06-30', 'Bodega'),
(8365753, 'Vicente', 'Gomez', '1990-07-21', 'Atención'),
(9543253, 'Andrea', 'Pizarro', '1968-05-23', 'Bodega'),
(10541453, 'Guillemo', 'Blake', '1982-08-14', 'Bodega'),		
(11549853, 'Angela', 'Davi', '1976-04-25', 'Ventas'),
(12545753, 'Luisa', 'Barrientos', '1991-09-15', 'Bodega'),
(130545753, 'Gabriel', 'Garcia', '1985-03-02', 'Bodega'),
(1445753, 'Diego', 'Velazquez', '1988-10-17', 'Atención'),
(1545753, 'Virginia', 'Lobos', '1979-01-28', 'Ventas'),
(1645753, 'Juana', 'Cruz', '1983-11-05', 'Ventas');

