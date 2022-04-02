# ABPro2



#  ----- Documentación -----



# 1)
# Clase Proveedor
# atributos:
# RUT
# Nombre Legal
# Razón Social
# País
# Una distinción entre persona jurídica o persona natural

class Proveedor():
	def __init__(self, rut, nombre_legal, razon_social, pais, persona):
		self.rut = rut
		self.nombre_legal = nombre_legal
		self.razon_social = razon_social
		self.pais = pais
		self.persona = persona

# 2)
# A las clases creadas en la actividad anterior,
# incorpore un atributo opcional a cada una.



# 3)
# Al momento de instanciar un objeto de la clase Producto,
# deberá existir una Composición con la clase Proveedor.



# 4)
# Se deberá crear un método vender de la clase Vendedor
# y esta deberá descontar el valor del atributo stock de la clase Producto
# y calcular un 0.5% de comisión referente al valor_neto del producto
# y luego sumarlo al atributo comisión de la clase Vendedor.
# Luego el método deberá calcular el valor final del producto
# y descontarlo del atributo saldo de la clase Cliente.

# 5)
# Se solicita que existan condicionales
# para realizar validaciones correspondientes,
# como por ejemplo si no existe saldo suficiente en la clase Cliente,
# este deberá mostrar un mensaje indicando
# que no es posible adquirir el producto por saldo insuficiente,
# de la misma forma para el stock de productos.

# 6)
# # Desarrolle cuatro métodos más para
# dinamizar la interacción entre diferentes clases e instancias.
# Al menos uno de estos métodos debe aplicar los contenidos de
# ‘sobrecarga de métodos’.



#  ----- Desarrollo -----



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       