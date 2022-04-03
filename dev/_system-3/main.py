class User():
    def __init__(self, id, nombre, dir):
        self.id = id
        self.nombre = nombre
        self.dir = dir
        
class Admin(User):
    def __init__(self, id, nombre, dir, cargo):
        super().__init__(id, nombre, dir)
        self.cargo = cargo



don_juan = Admin(135, 'Juan Perez', 'Calle 41', 'Administrador')



print(don_juan.id)
print(don_juan.nombre)
print(don_juan.dir)
print(don_juan.cargo)

