# ABP1


 
#  ----- Desarrollo -----



# 1)
# Identificación 3 tipos de usuarios:

# ADMINISTRADOR de la plataforma
# ASISTENTE de venta
# CLIENTE



# 2)
# Atributos y acciones por tipo de usuario

'''
ADMINISTRADOR

atributos:
clientes
asistentes
datos_servidor

métodos:
ver clientes
ver asistentes
ver datos_servidor
'''

class Administrador():

    def __init__(self, clientes, asistentes, datos_servidor):
        self.clientes = clientes
        self.asistentes = asistentes
        self.datos_servidor = datos_servidor

    def ver_clientes(self):
        print("\033[0;33m"+"-"*30)
        print("\033[0;33m"+"Clientes:")
        for x in self.clientes:
            print(f"\033[0;33m{x} - \033[1;33m{self.clientes[x][1]} - {self.clientes[x][2]}")
        print("\033[0;33m"+"-"*30+"\033[0;37m")


    def ver_asistentes(self):
        print("\033[0;36m"+"-"*30)
        print("\033[0;36m"+"Asistentes:")
        for x in self.asistentes:
            print(f"\033[0;36m{x} - \033[1;36m{self.asistentes[x][1]} - {self.asistentes[x][2]}")
        print("\033[0;36m"+"-"*30+"\033[0;37m")
            
    def ver_datos_servidor(self):
        print("\033[0;34m"+"-"*30)
        print("\033[0;34m"+"Datos servidor:")
        for x in self.datos_servidor:
            print(f"\033[0;34m{x} : \033[1;34m{self.datos_servidor[x]}")
        print("\033[0;34m"+"-"*30+"\033[0;37m")

'''
ASISTENTE

Atributos:
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
        print("\033[0;33m"+"-"*30)
        print("\033[0;33m"+"Clientes:")
        for x in self.clientes:
            print(f"\033[0;33m{x} - \033[1;33m{self.clientes[x][1]} - {self.clientes[x][2]}")
        print("\033[0;33m"+"-"*30+"\033[0;37m")

    def ver_preguntas(self):
        print("\033[0;36m"+"-"*30)
        print("\033[0;36m"+"Preguntas:")
        for x in self.preguntas:
            print(f"\033[0;36m{x} - \033[1;36m{self.preguntas[x][1]} - {self.preguntas[x][2]}")
        print("\033[0;36m"+"-"*30+"\033[0;37m")

    def ver_notas(self):
        print("\033[0;36m"+"-"*30)
        print("\033[0;36m"+"Notas:")
        for x in self.notas:
            print(f"\033[0;36m{x} - \033[1;36m{self.notas[x][1]} - {self.notas[x][2]}")
        print("\033[0;36m"+"-"*30+"\033[0;37m")

'''
CLIENTE

Atributos:
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
        print("\033[0;35m"+"-"*30)
        print("\033[0;35m"+"Catálogo de Productos:")
        for x in self.productos:
            print(f"\033[0;35msku: {x} - \033[1;35m{self.productos[x][1].title()}\033[0;35m: {self.productos[x][2]}")
        print("\033[0;35m"+"-"*30+"\033[0;37m")

    def ver_mi_usuario(self):
        print("\033[0;33m"+"-"*30)
        print("\033[0;33m"+"Mis datos de Usuario:")
        print("\033[0;33m"+"")
        print(f"\033[0;33mNombre: \033[1;33m{self.mi_usuario[1].title()}")
        print(f"\033[0;33mEmail: \033[1;33m{self.mi_usuario[2]}")
        print(f"\033[0;33mPassword: \033[1;33m{self.mi_usuario[3]}")
        print(f"\033[0;33mDirección: \033[1;33m{self.mi_usuario[4]}")
        print("\033[0;33m"+"-"*30+"\033[0;37m")
    
    def ver_hora(self):
        pass
        print(self.hora)
        print("\033[0;36m"+"-"*30)
        print("\033[0;36m"+"Hora:")
        print(f"\033[0;36m{self.hora}")
        print("\033[0;36m"+"-"*30+"\033[0;37m")


#  ----- Instaciación -----



# importacion de datos para de testeo
import test_data as td
# importacion modulo para generar hora actual
from datetime import datetime



administrador_1 = Administrador(td.data_clientes, td.data_asistentes, td.data_servidor)
# # print de testeo --------------------
# print(administrador_1.clientes)
# print(administrador_1.asistentes)
# print(administrador_1.datos_servidor)
# administrador_1.ver_clientes()
# administrador_1.ver_asistentes()
# administrador_1.ver_datos_servidor()



asistente_1 = Asistente(td.data_clientes, td.data_preguntas, td.data_notas)
asistente_2 = Asistente(td.data_clientes, td.data_preguntas, td.data_notas)
asistente_3 = Asistente(td.data_clientes, td.data_preguntas, td.data_notas)
# # print de testeo --------------------
# print(asistente_1.clientes)
# print(asistente_1.preguntas)
# print(asistente_1.notas)
# asistente_1.ver_clientes()
# asistente_1.ver_preguntas()
# asistente_1.ver_notas()


cliente_1 =  Cliente(td.data_productos, td.data_clientes[1], datetime.now())
cliente_2 =  Cliente(td.data_productos, td.data_clientes[2], datetime.now())
cliente_3 =  Cliente(td.data_productos, td.data_clientes[3], datetime.now())
cliente_4 =  Cliente(td.data_productos, td.data_clientes[4], datetime.now())
cliente_5 =  Cliente(td.data_productos, td.data_clientes[5], datetime.now())
# # print de testeo --------------------
# print(cliente_1.productos)
# print(cliente_1.mi_usuario)
# print(cliente_1.hora)
# cliente_1.ver_productos()
# cliente_1.ver_mi_usuario()
# cliente_1.ver_hora()





# 3)
# Nuevos atributos y acciones PENSADAS a realizar los objetos
# ADMINISTRADOR --> atributo: catálogo / métodos: bloquear tienda
# ASISTENTE --> atributo: catálogo / métodos: borrar nota
# CLIENTE --> atributo: catálogo / métodos: buscar producto




# 4)
# Gráfica de las relaciones entre las diferentes clases