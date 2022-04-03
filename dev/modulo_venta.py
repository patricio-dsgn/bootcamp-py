dataC = {
    1: ['andres', 123],
    2: ['bea', 642],
    3: ['camilo', 26624],
    4: ['david', 864],
    5: ['ester', 264624],
}

dataV = {
    1: ['lou', '@lou'],
    2: ['ada', '@ada'],
}

dataP = {
    1: ['manzana', 100],
    2: ['pera', 300],
    3: ['naranja', 800]
}


class Cliente:
    def __init__(self, id_cliente, nombre, saldo_disponible):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.saldo_disponible = saldo_disponible

    def comprar(self, id_prod):
        return self.id_cliente, id_prod


class Vendedor:
    def __init__(self, id_vendedor, nombre, mail):
        self.id_vendedor = id_vendedor
        self.nombre = nombre
        self.mail = mail

    def vender(self, id_prod):
        return self.id_vendedor, id_prod

class Producto:
    def __init__(self, id_prod, nombre, precio):
        self.id_prod = id_prod
        self.nombre = nombre
        self.precio = precio

    def vender(self, id_prod):
        return self.id_prod




class Nodo:
    def __init__(self, id_cliente, id_vendedor, id_producto):
        
        self.id_c = id_cliente
        self.id_v = id_vendedor
        self.id_p = id_producto

        
    def venta(self):
        c1 = Cliente(dataC[self.id_c], dataC[self.id_c][0],dataC[self.id_c][1])
        v1 = Vendedor(dataV[self.id_v], dataV[self.id_v][0],dataV[self.id_v][1])
        p1 = Producto(dataP[self.id_p], dataP[self.id_p][0],dataP[self.id_p][1])

        print('vendido')




venta1 = Nodo(1,2,3)



venta1.venta()

