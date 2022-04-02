# Control de Bodega

def crearBodega():
    '''- Crear una bodega virtual con los productos iniciales.'''
    bodega = {'ZAPATILLAS': [20, 'PARES'],
              'POLERAS': [10, 'UNIDADES'],
              'ZAPATOS': [15, 'PARES'],
              'POLERÓN': [3, 'UNIDADES'],
              'CHAQUETA': [5, 'UNIDADES'],
              'GUANTES': [4, 'PARES']
              }
    print("la bodega inicial es: ", bodega)
    return bodega


def almacenarNuevosProductos():
    '''Almacenar nuevos productos'''

    # todo: verificar que el producto ingresado no exista ya, de otro modo agregar unidad

    print("ingrese el producto, cantidad, y unidad")

    producto = input("\tingrese el producto")
    cantidad = input("\tingrese cantidad")
    cantidad = int(cantidad)
    unidad = input("\tingrese el tipo de unidad")

    return producto, cantidad, unidad


def actualizarStockVirtual(bodega: dict, producto: str, cantidad: int, unidad: str):
    # - Actualizar el stock de productos en la bodega virtual.
    bodega[producto] = [cantidad, unidad]
    return bodega


def unidadesDisponiblesProducto(bodega: dict):
    '''Mostrar y retornar las unidades disponibles de productos'''
    print("la bodega actualizada es: ")
    for key in bodega:
        print(f"\tcantidad producto {key} es {bodega[key][0]} {bodega[key][1]}")


def unidadesDisponiblesProductoParticular(bodega: dict):
    '''Mostrar y retornar las unidades disponibles de un producto en particular'''

    query = input("ingrese el producto que desea consultar stock: ")

    print("la cantidad de producto especifico: ")
    print(f"\tcantidad producto {query} es {bodega[query][0]} {bodega[query][1]}")


def mostrarProductos(bodega: dict):
    '''Mostrar y retornar todos los productos de la tienda.'''
    print("Los productos en bodega son: ", bodega.keys())


def mostrarProductosMayorCantidad(bodega: dict):
    '''Mostrar y retornar los productos que tienen más de un número de unidades (el usuario puede escoger el número de
    unidades).'''
    cantidad = input("Ingrese la cantidad minima de unidades de productos a mostrar")
    cantidad = int(cantidad)
    for key in bodega.keys():
        if bodega[key][0] >= cantidad:
            print(f"\tcantidad producto {key} es {bodega[key][0]} {bodega[key][1]}")





# Control de Ventas

# Nuestro programa deberá tener las siguientes funciones:
def agregarClientes(clientes: dict, cliente: str, producto: str, cantidad: int):
    '''funcion adicional que agrega clientes al sistema'''
    max_key_cliente = max(list(clientes.keys())) + 1
    clientes[max_key_cliente] = [cliente, producto, cantidad]
    try:
        clientes.pop(0)
    except Exception as error:
        #print(error)
        pass

    return clientes


def mostrarClientes(clientes: dict):
    # - mostrar y retornar el número de clientes registrados en la tienda.
    print("el numero de clientes en la tienda es: ", len(clientes.keys()))
    print(clientes)


def solicitarCompra(clientes: dict, cliente_id: int, bodega: dict):
    # - Funcionalidad para solicitar compra. Se ingresa el id del cliente, id del producto a comprar y las
    # unidades a comprar.
    # - respecto a la funcionalidad anterior, por defecto se comprará una unidad.
    ## - Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.

    producto_id = clientes[cliente_id][1]
    cantidad = clientes[cliente_id][2]

    if cantidad == None:
        cantidad = 1
    if cantidad <= 0:
        cantidad = 1
    if cantidad <= bodega[producto_id][0]:
        print(f'hay stock disponible de {producto_id} para la cantidad {str(cantidad)} para el cliente {clientes[cliente_id][0]}')
        return True
    else:
        print(f'No hay stock disponible de {producto_id} para la cantidad {str(cantidad)} para el cliente {clientes[cliente_id][0]}')
        return False


# - Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega
# virtual.


def compraBool(hay_stock):
    # - Imprimir y retornar un mensaje “Compra aprobada y en camino” en caso que exista el stock
    # necesario.
    if hay_stock == True:
        print("Compra aprobada y en camino")
    # - Imprimir y retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.

    if hay_stock == False:
        print("Compra cancelada")

