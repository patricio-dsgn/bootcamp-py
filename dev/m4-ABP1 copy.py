# ABP1
 
 

#  ----- Documentación -----



# 1)
# Identificación 3 tipos de usuarios:

# ADMINISTRADOR de la plataforma
# ASISTENTE de venta
# CLIENTE



# 2)
# Atributos por tipo de usuario
# ADMINISTRADOR: lista clientes, lista asistentes, datos servidor
# ASISTENTE: lista clientes, libro de preguntas, libro de notas
# CLIENTE: dirección, historial, carro de compra



# 3)
# Identifica 3 acciones que pueden desarrollar cada tipo de usuario.
# ADMINISTRADOR: ver usuarios, agregar usuario, quitar usuario
# ASISTENTE: ver preguntas ,responder pregunta ,crear nota
# CLIENTE: elegir producto, pagar producto, hacer pregunta



# 4) nuevos atributos y acciones a realizar los objetos
# • ADMINISTRADOR atributo: catálogo / acción: bloquear tienda
# • ASISTENTE atributo: catálogo / acción: borrar nota
# • CLIENTE atributo: catálogo / acción: buscar producto



# 5)
# Piensen en una forma de graficar las
# relaciones entre las diferentes clases,
# puede ser un diagrama o gráfica.
# Desarrollen el ejercicio de forma intuitiva.



#  ----- Desarrollo -----

# datos de prueba
import test_data

# funciones para hacer cosas especiales
import extra_functions



# clase "general"
class User():
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
 
    def sign_in(self):
        extra_functions.card('identificate')
        in_email = input("email: ")
        in_password = input("password: ")
        if(in_email == self.email and in_password == self.password):
            extra_functions.card('ingresaste')
        else:
            extra_functions.card('denegado')

    def sign_out(self):
        in_exit = input("¿Deseas salir?: ").lower()
        if(in_exit == 'si'):
            extra_functions.card('Has salido de la plataforma')


class Admin(User):
    def __init__(self, id, name, email, password, customers, asistants, data_server):
        self.customers = customers
        self.asistants = asistants
        self.data_server = data_server
        super().__init__(id, name, email, password)        

    def view_user(self):
        test_data.fake_customers

    def create_user(self):
        test_data.fake_asistants
        test_data.fake_data_server
        pass

    def delete_user(self):
        pass



class Asistant(User):
    def __init__(self, id, name, email, password, customers, questions, notes):
        self.customers = customers
        self.questions = questions
        self.notes = notes
        super().__init__(id, name, email, password)        

    def view_questions():
        pass

    def response_question():
        pass

    def create_note():
        pass


class Cliente(User):
    def __init__(self, id, name, email, password, direction, historial, cart):
        self.direction = direction
        self.historial = historial
        self.cart = cart
        super().__init__(id, name, email, password)        

    def sel_product():
        pass

    def pay_product():
        pass

    def make_question():
        pass








# print(admin.id)
# print(admin.name)
# print(admin.email)
# print(admin.password)
# print(admin.customers)
# print(admin.asistants)
# print(admin.data_server)



# class Asistant(User):
#     def __init__(self):
#         pass
#     def answer():
#         pass
#     def delivery():
#         pass

# class Client(User):
#     def __init__(self):
#         pass
#     def question():
#         pass
#     def buy():
#         pass
#     def buyCancel():
#         pass


# a1 = Asistant('Warrior', 'warrior@mail.com','odioestetrabajo11')
# a2 = Asistant('Mario', 'marioallstarts@mail.com','tortugas11')
# a3 = Asistant('Luigi', 'superluigi@mail.com','tortugas12')

# u1 = Client('Carade', 'cara@mail.com','talcual')
# u2 = Client('Maiga', 'maiga@mail.com','asinomas')
# u3 = Client('Mojojojo', 'mojojojo@mail.com','quetepa')
# u4 = Client('Calila', 'calila@mail.com','corta')


# Las acciones se deben ejecutar de forma interna
#  en nuestra aplicación.
# Por ejemplo, acceder a datos sensibles,
# registrar nuevos usuarios,
# enviar solicitudes de información adicional.

# ● Piense en nuevos atributos y acciones que
#  pueden realizar los objetos.

# Piensen en una forma de graficar las relaciones
#  entre las diferentes clases,
#  puede ser un diagrama o gráfica.
#  Desarrollen el ejercicio de forma intuitiva.
