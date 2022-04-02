import random

# Control de Bodega
def crearBodega():
    '''- Crear una bodega virtual con los productos iniciales.'''
    bodega = {'vasos': [random.randint(300, 500), "Vaso: Alto 255 ml liso 6 unidades"],
              'cucharas': [random.randint(300, 500), "Cucharas: Para helados, 20,8 cm"],
              'cuchillos': [random.randint(300, 500), "Cuchillos: Chef, Hoja de acero inoxidable, 34 cm"],
              'tenedores': [random.randint(300, 500), "Tenedores: Acero inoxidable / madera natura"]
              }
    print("la bodega inicial es: ", bodega)
    print("\n")
    return bodega

def alertaStock(stock):
    '''- Mostrar una alerta de stock en la bodega.'''
    if stock < 400:
        print("\t***Alerta de stock: ", stock)

def mostarStock(bodega):
    '''- Mostrar el stock de la bodega.'''
    print("Stock de la bodega: ")
    for key in bodega.keys():
        print(key, ": ", bodega[key])
        alertaStock(bodega[key][0])
    print("\n")

def addElemento(bodega:dict, elemento: str, cantidad: int, descripcion: str):
    '''- Agregar un elemento a la bodega.'''
    print("Agregando productos")
    if elemento in bodega.keys():
        bodega[elemento][0] += cantidad
        print("\tSe agregó adicionalmente: ", elemento, ": ", cantidad)
        if bodega[elemento][1] == None:
            bodega[elemento][1] = descripcion
        if bodega[elemento][1] == '':
            bodega[elemento][1] = descripcion
        else:
            print("\tDescripción ", descripcion, "descartada")
    else:
        bodega[elemento] = [cantidad, descripcion]
        print("\tSe agregó: ", elemento, ": ", cantidad)
        alertaStock(cantidad)
    print("\n")


def removeElemento(bodega:dict, elemento: str, cantidad: int):
    '''- Remover un elemento a la bodega.'''
    print("Removiendo productos")
    if elemento in bodega.keys():
        bodega[elemento][0] -= cantidad
        print("\tSe removió : ", elemento, ": ", cantidad)
        alertaStock(bodega[elemento][0])
    else:
        print("\tNo se encontró el elemento: ", elemento)
    print("\n")


bodega = crearBodega()
addElemento(bodega = bodega, elemento = 'pincho', cantidad = 2, descripcion = 'Pincho: Para asado, 20,8 cm')
addElemento(bodega = bodega, elemento = 'tenedores', cantidad = 1, descripcion = 'reemplazando descripcion')
removeElemento(bodega = bodega, elemento = 'cucharas', cantidad = 200)
removeElemento(bodega = bodega, elemento = 'martillo', cantidad = 200)
mostarStock(bodega)

