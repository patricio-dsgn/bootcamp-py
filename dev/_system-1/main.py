class User():
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def opinar(self, txt):
        print(txt)

andres = User(1, 'Andrés')
benito = User(2, 'Benito')
camila = User(2, 'Camila')

