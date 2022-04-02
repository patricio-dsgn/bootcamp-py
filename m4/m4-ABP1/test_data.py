# datos de servidor
data_servidor = {
    'ip' : '425.653.365.356',
    'space' : 1100,
    'bandwidth': 15,
}

# datos usuarios - - - - - -

# datos admin
data_administrador = {
    #'id' : ['tipo', 'nombre', 'email', 'password', 'address']
    1: ['administardor', 'jefe', 'jefe@mail.cl', '1234', None]
}

# datos asistentes
data_asistentes = {
    #'id' : ['tipo', 'nombre', 'email', 'password', 'address']
    1 : ['asistente', 'fernando', 'fernando@mail.cl', '111', None],
    2 : ['asistente', 'gabriela', 'gabriela@mail.cl', '222', None],
    3 : ['asistente', 'hilda', 'hilda@mail.cl', '333', None]
}

# datos clientes
data_clientes = {
    # 'tipo', 'id', 'nombre', 'email', 'password', 'address'
    1 : ['cliente', 'andres', 'andres@mail.cl', '1234', 'dir1'],
    2 : ['cliente', 'berta', 'berta@mail.cl', '1234', 'dir2'],
    3 : ['cliente', 'camila', 'camila@mail.cl', '1234', 'dir3'],
    4 : ['cliente', 'david', 'david@mail.cl', '1234', 'dir4'],
    5 : ['cliente', 'eva', 'eva@mail.cl', '1234', 'dir5']
}

# datos productos
data_productos = {
    # tipo, id, nombre, descripción, stock, price
    1 : ['producto','galletas chocolate', 'contiene trozos de chocolate', 930, 230],
    2 : ['producto','galletas limon', 'contiene trozos de limon', 404, 204],
    3 : ['producto','galletas platano', 'contiene trozos de platano', 224, 200],
    4 : ['producto','galletas zanahoria', 'contiene trozos de zanahoria', 554, 254],
    5 : ['producto','galletas avena', 'contiene trozos de avena', 130, 230]
}


# datos preguntas
data_preguntas = {
    # tipo, id, nombre, descripción, id_producto, id_cliente
    1 : ['pregunta', 'chocolate blanco', '¿tienen de chocolate blanco?', 2, 2],
    2 : ['pregunta', 'chips limon', '¿son chips limon o escencia?', 5, 1],
    3 : ['pregunta', 'horario atención', '¿abren los domingos?', 1, 3]
}

# datos notas
data_notas = {
    # tipo, id, nombre, descripción, id_producto, id_cliente, id_vendedor
    1 : ['nota','chocolate', 'muchos clientes piden de chocolate blanco', 2, 2],
    2 : ['nota','limon', 'no les gustan los trozos de limon', 3, 2],
    3 : ['nota','domindos abierto', 'preguntan por horario de atencion', 1, 2]
}

