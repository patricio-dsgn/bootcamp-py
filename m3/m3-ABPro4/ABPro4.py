# DESARROLLO

# Hoy simularemos que nuestra tienda virtual tiene muchos usuarios comprando desesperadamente. De
# igual forma, simularemos un alto movimiento de proveedores que renuevan nuestro stock de productos
# a ofrecer.

# Primero, desarrollaremos una forma de almacenar nuestro stock de dos productos. El primer producto
# tendrá 120 unidades y el segundo 150.

# Luego, simularemos cada 3 segundos una compra de “n” unidades de cualquiera de los dos productos.
# n representa un número aleatorio entre 1 y 10.

# Cada compra, como es natural, afecta el stock inicial de productos. Es decir, si una compra simulada es
# de 3 unidades del producto 1, este se debe descontar del stock.

# Cada 10 compras, el programa debe imprimir en pantalla el número de unidades disponibles por producto.

# ¿Lo lograron?

# Por último, cuando un producto tenga un stock de menos de 100 unidades, los proveedores enviarán
# automáticamente 50 unidades más. Esto se debe reflejar en el stock de cada producto.

# Lamentablemente, los proveedores solo tienen stock suficiente para enviar 150 unidades en total de
# productos 1 y 2.

# ¡Buena suerte desarrolladores!

import time
import random

producto1 = 120
producto2 = 150
contador = 0
contador_compras = 0
cantidad_de_ventas = 0
cantidad_de_productos_vendidos = 0

while True:
    # n es la cantidad de compra
    n = random.randint(1, 10)
    # producto es el producto que se compra (1 para producto1, 2 para producto2)
    producto = random.randint(1, 2)

    # si el producto = 1, se descuenta del producto1
    if producto == 1:
        producto1 = producto1 - n

        # si el stock de producto1 es menor a 100, se envia 50 unidades
        if producto1 < 100:
            producto1 = producto1 + 50
            print("\nSe ha enviado 50 unidades de producto 1")
            # se actualiza el contador de reposición
            contador = contador + 1

    if producto == 2:
        producto2 = producto2 - n
        if producto2 < 100:
            producto2 = producto2 + 50
            print("\nSe ha enviado 50 unidades de producto 2")
            contador = contador + 1

    # se incrementa el contador de compras
    contador_compras = contador_compras + 1

    # se incrementa la cantidad de ventas
    cantidad_de_ventas = cantidad_de_ventas + 1

    # se consolida la cantidade de productos ventidos
    cantidad_de_productos_vendidos = cantidad_de_productos_vendidos + n

    # si el contador de reposición es 3, se imprime el stock de producto1 y producto2
    # y se finaliza el programa
    if contador == 3:
        print("\nResultado final:")
        print("cantidad de ventas:", cantidad_de_ventas)
        print("cantidad total de productos vendidos:", cantidad_de_productos_vendidos)
        print("Producto 1:", producto1)
        print("Producto 2:", producto2)
        print("Fin del programa")
        break

    # cada 10 compras, se imprime el stock de producto1 y producto2
    if contador_compras == 10:
        contador_compras = 0
        print("\nStock de productos:")
        print("cantidad de ventas:", cantidad_de_ventas)
        print("cantidad total de productos vendidos:", cantidad_de_productos_vendidos)
        print("Producto 1:", producto1)
        print("Producto 2:", producto2)

    # se espera 3 segundos para la siguiente compra
    time.sleep(3)

