from time import sleep


class Vendedor: 

    def __init__(self, id, nombre, ventas):
        self.id = id
        self.nombre = nombre
        self.ventas = ventas
    
    def vender(self):
        pass



class Caja: 

    def __init__(self, sku, ventas):
        self.sku = sku
        self.ventas = ventas
    
    def venta(self):
        pass

print(538667)
print(538667)
print(538667)
print(538667)

sleep(1)

def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

clear()


vendedor_1 = Vendedor('juan', 'perez', 34)
caja_1 = Caja(475, 6)


# juan.telefono = 968359053

# print(juan.telefono)




