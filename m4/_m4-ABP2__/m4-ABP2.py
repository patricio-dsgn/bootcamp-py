# ABP1
 
 

#  ----- Desarrollo -----



# 1)
# Identificación 3 tipos de usuarios:

# ADMINISTRADOR de la plataforma
# ASISTENTE de venta
# CLIENTE



# 2)
# atributos y acciones por tipo de usuario

'''
ADMINISTRADOR

atributos:
lista clientes
lista asistentes
datos servidor

métodos:
ver lista clientes
ver lista asistentes
ver lista datos servidor
'''

class Administrador():

    def __init__(self, clientes, asistentes, datos_servidor):
        self.clientes = clientes
        self.asistentes = asistentes
        self.datos_servidor = datos_servidor

    def ver_clientes(self):
        for x in self.clientes:
            print(x)

    def ver_asistentes(self):
        for x in self.asistentes:
            print(x)

    def ver_datos_servidor(self):
        for x in self.datos_servidor:
            print(x)

'''
ASISTENTE

atributos:
lista clientes
libro de preguntas
libro de notas

métodos
ver lista clientes
ver libro de preguntas
ver libro de notas
'''

class Asistente():

    def __init__(self, clientes, preguntas, notas):
        self.clientes = clientes
        self.preguntas = preguntas
        self.notas = notas

    def ver_clientes(self):
        for x in self.clientes:
            print(x)

    def ver_preguntas(self):
        for x in self.preguntas:
            print(x)

    def ver_notas(self):
        for x in self.notas:
            print(x)

'''
CLIENTE

atributos:
productos
mi usuario
hora

métodos:
ver lista productos
ver mi usuario
ver hora
'''

class Cliente():

    def __init__(self, productos, mi_usuario, hora):
        self.productos = productos
        self.mi_usuario = mi_usuario
        self.hora = hora

    def ver_productos(self):
        for x in self.productos:
            print(x)

    def ver_mi_usuario(self):
        for x in self.mi_usuario:
            print(x)

    def ver_hora(self):
        print(self.hora)


'''
REPARTIDOR

atributos:
envios realizados
envios pendientes
vehiculo
horario(opcional)

métodos:
mostrar ubicacion
mostrar kilometros recorridos
mostrar capacidad disponible
emitir alerta de problema en entrega
'''

class Repartidor():

    def __init__(self, envios_realizados, envios_pendientes, vehiculo, horario=None):
        if horario is None:
            self.horario = 'normal'

        self.envios_realizados = envios_realizados
        self.envios_pendientes = envios_pendientes
        self.vehiculo = vehiculo
        self.horario = horario

    def mostrar_ubicacion(self):
        print('ubicacion: 682, 971')

    def mostrar_kilometros_recorridos(self):
        print('km recorridos')

    def mostrar_capacidad_disponible(self):
        print("80% de capacidad")

    def emitir_alerta_de_problema_en_entrega(self):
        input('escriba su alerta: ')



#  ----- Instaciación -----



# importacion de datos para de testeo
import test_data as td
# importacion modulo para generar hora actual
from datetime import datetime

administrador_1 = Administrador(td.data_clients, td.data_asistants, td.data_server)

asistente_1 = Asistente(td.data_clients, td.data_questions, td.data_notes)
asistente_2 = Asistente(td.data_clients, td.data_questions, td.data_notes)
asistente_3 = Asistente(td.data_clients, td.data_questions, td.data_notes)

cliente_1 =  Cliente(td.data_products, td.data_clients[0], datetime.now())
cliente_2 =  Cliente(td.data_products, td.data_clients[1], datetime.now())
cliente_3 =  Cliente(td.data_products, td.data_clients[2], datetime.now())
cliente_4 =  Cliente(td.data_products, td.data_clients[3], datetime.now())
cliente_5 =  Cliente(td.data_products, td.data_clients[4], datetime.now())


repartidor_1 = Repartidor()


print(repartidor_1.envios_realizados)
print(repartidor_1.envios_pendientes)
print(repartidor_1.vehiculo)
print(repartidor_1.horario)
repartidor_1.mostrar_ubicacion()
repartidor_1.mostrar_kilometros_recorridos()
repartidor_1.mostrar_capacidad_disponible()
repartidor_1.emitir_alerta_de_problema_en_entrega()



# 3)
# Nuevos atributos y acciones a realizar los objetos
# ADMINISTRADOR --> atributo: catálogo / métodos: bloquear tienda
# ASISTENTE --> atributo: catálogo / métodos: borrar nota
# CLIENTE --> atributo: catálogo / métodos: buscar producto

catalogue_especial = ['catalogue_especial']

def bloquear():
    print('tienda bloqueada')
fun_bloquear = bloquear

def borrar_notas():
    print('nota borrada')
fun_borrar_notas = borrar_notas

def buscar_productos():
    print('nota buscando producto')
fun_buscar_productos = buscar_productos


# atributo catalogo
administrador_1.catalogue = catalogue_especial
asistente_1.catalogue = catalogue_especial
cliente_1.catalogue = catalogue_especial

# metodo bloquear tienda
administrador_1.bloquear = fun_bloquear
# metodo borrar nota
asistente_1.borrar_notas = fun_borrar_notas
# metodo buscar producto
cliente_1.buscar_productos = fun_buscar_productos



# 4)
# Gráfica de las relaciones entre las diferentes clases