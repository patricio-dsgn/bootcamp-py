def saludar():
    return print('hola!')

x = saludar



class User: 
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
juan = User('juan', 'perez')



juan.telefono = 968359053
juan.hablar = x

# print(juan.telefono)
juan.hablar()




