# 3. Sistema de envío
 

# ESTA ES UNA PROPUESTA

def ElegirBodega(distancia):
    if distancia > 1000:
        return 'largo'
    else:
        return 'rapido'


def GuardadoBodega(
    test,
    tipo,
    id_cliente,
    producto,
    cantidad,
    direccion,
    distancia,
    bodega_A,
    bodega_B):

    if(test):
        if tipo == 'rapido':
            bodega_B.append([id_cliente, producto, cantidad, direccion, distancia])

        elif tipo =='largo':
            bodega_A.append([id_cliente, producto, cantidad, direccion, distancia])




def verificaBodega(cantidad, tipo, bodega_A, bodega_B):

    if tipo == 'rapido':
        n = len(bodega_B) + cantidad
        if(n < 500):
            return True
        else:
            print("\nBodega B no tiene capacidad")
            print("no se guardó\n")
            return False

    elif tipo == 'largo':
        n = len(bodega_A) + cantidad
        if(n < 500):
            return True
        else:
            print("\nBodega A no tiene capacidad")
            print("no se guardó\n")
            return False


def verPedidosBodegas(bodega_A, bodega_B):
    print("\n")
    print(f"\"Bodega A: {len(bodega_A)} ")
    print(f"\"Bodega B: {len(bodega_B)} ")
    print("\n")


# -------------------



# Bodegas: bodega_A, bodega_B
# id cliente, producto, cantidad, dirección, distancia
# ejemplo con 4 pedidos en bodega
bodega_A = [
    [10, "vasos", 111, "dir1", 4000 ],
    [1, "cucharas", 13, "dir2", 2000],
    [25, "cuchillos", 116, "dir3", 2400],
    [4, "tenedores", 141, "dir4", 3000]
]

# ejemplo con 6 pedidos en bodega
bodega_B = [
    [20, "vasos", 111, "dir1", 100 ],
    [34, "cucharas", 23, "dir2", 200],
    [34, "cucharas", 33, "dir2", 20],
    [23, "tenedores", 441, "dir4", 120],
    [15, "cuchillos", 216, "dir3", 400],
    [5, "cuchillos", 116, "dir3", 400]
]

verPedidosBodegas(bodega_A, bodega_B)

distancia = int(input("distancia en Km: "))
cantidad = int(input("cantidad: "))
id_cliente = 11 # datos para testeo
producto = 'ejemplo' # datos para testeo
direccion = 'calle x' # datos para testeo

tipo = ElegirBodega(distancia)

test = verificaBodega(cantidad, tipo, bodega_A, bodega_B)

GuardadoBodega(
    test,
    tipo,
    id_cliente,
    producto,
    cantidad,
    direccion,
    distancia,
    bodega_A,
    bodega_B
)

verPedidosBodegas(bodega_A, bodega_B)
