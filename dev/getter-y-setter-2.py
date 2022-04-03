# Getter 

class User: 

    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self.__apellido = apellido
    
    @property
    def t1(self):
        return(self.__apellido)



juan = User('juan', 'perez')


print(juan.t1)


# juan.telefono = 968359053

# print(juan.telefono)




