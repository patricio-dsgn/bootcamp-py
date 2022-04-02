#  {ID: ['nombre', 'apellido', 'edad', 'contraseña']}
clientes = {0:  ['nombre', 'apellido', 'edad', 'contraseña'],
            1: ['carlos', 'shahe', 33, '12345'],
            2: ['andres', 'tinto', 32, '12335'],
            3: ['carlos', 'turro', 2, '12345'],
            4: ['ummat', 'sarrett', 45, '12345']
            }


def agregarClientes(clientes: dict, nombre: str, apellido: str, edad: int, contrasena: str):
    '''funcion adicional que agrega clientes al sistema'''
    max_key_cliente = max(list(clientes.keys())) + 1
    clientes[max_key_cliente] = [nombre, apellido, edad, contrasena]
    try:
        clientes.pop(0)
    except Exception as error:
        #print(error)
        pass

    return clientes

def quitarClientes(clientes: dict, id: int):
    '''funcion adicional que elimina clientes al sistema'''


    try:
        print('eliminando cliente con id: ', id)
        print('el cliente eliminado es: ', clientes[id])
        clientes.pop(id)
    except:
        print('No existe el cliente')
    return clientes


def mostrarClientes(clientes: dict):
    '''funcion que muestra los clientes'''
    for key, value in clientes.items():
        print(key, value)


#clientes = agregarClientes(clientes =clientes, nombre = 'carlos', apellido='shahe', edad = 33, contrasena= '12345')
#clientes = agregarClientes(clientes =clientes, nombre = 'andres', apellido='tinto', edad = 32, contrasena= '12335')
#clientes = agregarClientes(clientes =clientes, nombre = 'carlos', apellido='turro', edad = 2, contrasena= '12345')
clientes = agregarClientes(clientes =clientes, nombre = 'pepe', apellido='sarrett', edad = 45, contrasena= '1234234235')
clientes = quitarClientes(clientes = clientes, id= 434)
mostrarClientes(clientes = clientes)