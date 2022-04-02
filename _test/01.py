class Casa:

    def __init__(self,a_,b_):
        self.direccion = a_
        self._dueno = b_

    # def saludar(self):
    #     print("¡Hola, mundo!")


class Tipo(Casa):
    def __init__(self,a_,b_,c_):
        super().__init__(a_,b_)
        self.tipo = c_

    # def saludar(self):
    #     print("¡Hola, mundo!")

ca = Tipo('calle 111','juan','mansion')
print(ca.tipo)



