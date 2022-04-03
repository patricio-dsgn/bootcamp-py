

# Getter 

class User: 

    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self.__apellido = apellido
    
    # @property
    # def t1(self):
    #     return(self.__apellido)

    # @t1.setter
    def set(self, nuevo):
        self.__apellido = nuevo


juan = User('juan', 'perez')

juan.t1 = 'rojas'

print(juan.t1)


# juan.telefono = 968359053

# print(juan.telefono)




