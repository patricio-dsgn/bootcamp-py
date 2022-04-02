# Sistema de envío
# ● El sistema de envío debe ser un programa que pregunta qué tipo de envío es necesario (Rápido o largo)
# ● Si es un envío a una distancia de más de 1.000 km es considerado largo. Si es igual o menor a la distancia
# de 1.000 km es considerado rápido.
# ● En el caso que sea un envío rápido debe enviarse a una Bodega_A, caso contrario debe ser almacenado a una Bodega_B.
# ● El programa debe verificar que cada bodega no supere las 500 unidades.

def crearBodega():
    bodega_a = {0: ["Producto A", 0, 0, "Direccion A"]}
    bodega_b = {0: ["Producto B", 0, 0, "Direccion B"]}
    return bodega_a, bodega_b


# ejemplo de bodega_a = {1: ["producto", "cantidad", "distancia", "direccion"]}
# ejemplo de bodega_b = {1: ["tenedor", 100, 1000,"caca 123"]}

def mostrarBodega(bodega_a, bodega_b):
    print("Bodega A: ", bodega_a)
    print("Bodega B: ", bodega_b)

def comprobarCantidad(bodega):
    '''funcion que cuenta la cantidad de productos en la bodega'''
    cantidad_en_bodega = 0
    for key in bodega:
        cantidad_en_bodega += bodega[key][1]
    return cantidad_en_bodega


def agregarBodega(bodega_a, bodega_b):

    nom_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    distancia = int(input("Ingrese la distancia: "))
    direccion = input("Ingrese la dirección: ")

    if distancia > 1000:
        print("Envio a largo")
        print("se debe agregar a la bodega B")
        cantidad_en_bodega = comprobarCantidad(bodega_b)
        if (cantidad_en_bodega + cantidad) > 500:
            print("No se puede agregar, la bodega B quedaría sobrepasada en capacidad")
            exit()
        else:
            id = max(bodega_b.keys()) + 1
            bodega_b[id] = [nom_producto, cantidad, distancia, direccion]
            print("Se agregó correctamente a la bodega B")
    else:
        print("Envio a rápido")
        print("se debe agregar a la bodega A")
        cantidad_en_bodega = comprobarCantidad(bodega_a)
        if (cantidad_en_bodega + cantidad) > 500:
            print("No se puede agregar, la bodega A quedaría sobrepasada en capacidad")
            exit()
        else:
            id = max(bodega_a.keys()) + 1
            bodega_a[id] = [nom_producto, cantidad, distancia, direccion]
            print("Se agregó correctamente a la bodega A")

    return bodega_a, bodega_b

bodega_a, bodega_b = crearBodega()
mostrarBodega(bodega_a, bodega_b)
bodega_a, bodega_b = agregarBodega(bodega_a, bodega_b)
mostrarBodega(bodega_a, bodega_b)
bodega_a, bodega_b = agregarBodega(bodega_a, bodega_b)
mostrarBodega(bodega_a, bodega_b)