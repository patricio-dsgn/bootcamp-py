# DESARROLLO
# ● Como se mencionó anteriormente, es necesario mejorar el rendimiento de la empresa. Nuestro
# socio se percató que hay mucho código que se repite una y otra vez, lo que dificulta el mantenimiento
# de los programas.


# modulo con funciones
import modulo_pato as mp





# iniciar bodega
bodega_inicial = mp.crearBodega()

# definir productos nuevos
nuevo_producto, nuevo_cantidad, nuevo_unidad = mp.almacenarNuevosProductos()

# agregar productos a bodega
bodega = mp.actualizarStockVirtual(bodega_inicial, nuevo_producto, nuevo_cantidad, nuevo_unidad)

# - Mostrar y retornar las unidades disponibles por producto.
mp.unidadesDisponiblesProducto(bodega)

# - Mostrar y retornar las unidades disponibles de un producto en particular.
mp.unidadesDisponiblesProductoParticular(bodega)

# - Mostrar y retornar todos los productos de la tienda.
mp.mostrarProductos(bodega)

# - Mostrar y retornar los productos que tienen más de un número de unidades (el usuario puede
# escoger el número de unidades).
mp.mostrarProductosMayorCantidad(bodega)





# {id: [usuario, producto, cantidad]}
clientes = {0: ['ADMIN', 'PRODUCTOS', 1]}

mp.agregarClientes(clientes, 'pepito', 'POLERAS', 10)
mp.agregarClientes(clientes, 'juan', 'ZAPATILLAS', 1)
mp.agregarClientes(clientes, 'ardillo', 'POLERAS', 100)
mp.agregarClientes(clientes, 'murci', 'ZAPATILLAS', 1000)
mp.agregarClientes(clientes, 'alexis', 'CHAQUETA', 11)

# Nuestro programa deberá tener las siguientes funciones:
# - mostrar y retornar el número de clientes registrados en la tienda.

mp.mostrarClientes(clientes)

# - Funcionalidad para solicitar compra. Se ingresa el id del cliente, id del producto a comprar y las
# unidades a comprar.
# - respecto a la funcionalidad anterior, por defecto se comprará una unidad.
# - Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.
hay_stock_bool = mp.solicitarCompra(clientes=clientes, cliente_id=3, bodega=bodega)

# - Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega
# virtual.
# - Imprimir y retornar un mensaje “Compra aprobada y en camino” en caso que exista el stock
# necesario.
# - Imprimir y retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.
mp.compraBool(hay_stock_bool)