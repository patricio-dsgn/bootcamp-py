class User():
    def __init__(self, id, nombre, dir):
        self.id = id          # publico
        self._nombre = nombre # protegido
        self.__dir = dir      # privado



don_juan = User(135, 'Juan Perez', 'Calle 41')



print(don_juan.id)         # publico
print(don_juan._nombre)    # protegido: _atributo
print(don_juan._User__dir) # privado: _Clase__atributo