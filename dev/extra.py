
fake_customers = {
    161: ['andres', 'dir1'],
    234: ['berta', 'dir2'],
    362: ['camila', 'dir3'],
    834: ['david', 'dir4'],
    661: ['eva', 'dir5'],
}

fake_asistants = {
    1: ['fernando'],
    2: ['gabriela'],
    3: ['hilda'],

}

fake_data_server = {
    'ip': '425.653.365.356',
    'space': 100,
    'bandwidth': 5,
}




class User():
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.__email = email
        self.password = password
 
    def sign_in(self):
        card('identificate')
        in_email = input("email: ")
        in_password = input("password: ")
        if(in_email == self.email and in_password == self.password):
            card('ingresaste')
        else:
            card('denegado')

    def sign_out(self):
        in_exit = input("¿Deseas salir?: ").lower()
        if(in_exit == 'si'):
            card('Has salido de la plataforma')


class Admin(User):
    def __init__(self, id, name, email, password, customers, asistants, data_server):
        self.customers = customers
        self.asistants = asistants
        self.data_server = data_server
        super().__init__(id, name, email, password)        

    def view_user():
        pass

    def add_and_delete_user():
        pass

    def blockStore():
        pass


admin = Admin(76542, 'DonJuan', 'jefe@mail.com', '1234', 'dic_clientes', 'dic_asistentes', 'dic_data_server')

# print(admin.id)
# print(admin.name)
# print(admin.email)
# print(admin.password)
# print(admin.customers)
# print(admin.asistants)
# print(admin.data_server)

admin.sign_in()

admin.sign_out()


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
