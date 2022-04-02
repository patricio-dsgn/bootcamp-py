# datos falsoss de servidor
# ip, space, bandwidth
data_servidor = [
    '425.653.365.356',
    1100,
    15,
]


# datos usuarios
data_administradores = [
    # datos admin
    # 'type', 'id', 'name', 'email', 'password', 'address'
    ['admin', 0, 'jefe', 'jefe@mail.cl', '1234'],
]

data_asistentes = [    
    # datos asistentes
    # 'type', 'id', 'name', 'email', 'password', 'address'
    ['asistant', 1, 'fernando', 'fernando@mail.cl', '1234'],
    ['asistant', 2, 'gabriela', 'gabriela@mail.cl', '1234'],
    ['asistant', 3, 'hilda', 'hilda@mail.cl', '1234']
]

data_clientes = [
    # datos clientes
    # 'type', 'id', 'name', 'email', 'password', 'address'
    ['client', 161, 'andres', 'andres@mail.cl', '1234', 'dir1'],
    ['client', 234, 'berta', 'berta@mail.cl', '1234', 'dir2'],
    ['client', 362, 'camila', 'camila@mail.cl', '1234', 'dir3'],
    ['client', 834, 'david', 'david@mail.cl', '1234', 'dir4'],
    ['client', 661, 'eva', 'eva@mail.cl', '1234', 'dir5']
]


# datos productos
data_productos = [
    # type, id, name, description, stock, price
    ['product',1, 'galletas chocolate', 'contiene trozos de chocolate', 930, 230],
    ['product',2, 'galletas limon', 'contiene trozos de limon', 404, 204],
    ['product',3, 'galletas platano', 'contiene trozos de platano', 224, 200],
    ['product',4, 'galletas zanahoria', 'contiene trozos de zanahoria', 554, 254],
    ['product',5, 'galletas avena', 'contiene trozos de avena', 130, 230]
]


# datos preguntas
data_preguntas = [
    # type, id, name, description, id_product, id_client
    ['question',1, 'chocolate blanco', '¿tienen de chocolate blanco?', 2, 234],
    ['question',2, 'chips limon', '¿son chips limon o escencia?', 5, 362],
    ['question',3, 'horario atención', '¿abren los domingos?', 1, 834]
]

# datos notas
data_notas = [
    # type, id, name, description, id_product, id_client
    ['note',1, 'chocolate', 'muchos clientes piden de chocolate blanco', 2],
    ['note',2, 'limon', 'no les gustan los trozos de limon', 3],
    ['note',3, 'domindos abierto', 'preguntan por horario de atencion', 1]
]




data_clientes = [
    # datos clientes
    # 'type', 'id', 'name', 'email', 'password', 'address'
    ['delivery', 161, 'andres', 'andres@mail.cl', '1234', 'dir1'],
    ['delivery', 234, 'berta', 'berta@mail.cl', '1234', 'dir2'],
]




# datos productos especiales
data_productos_especiales = [
    # type, id, name, description, stock, price
    ['product',2, 'galletas con manjar', 'rellenas de manjar', 404, 204],
    ['product',3, 'galletas con nutella', 'rellenas de nutella', 704, 304],
]