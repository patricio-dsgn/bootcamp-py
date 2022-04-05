# ABP5 - - - - - - - - - - 



# 1)
# En el diagrama integra una estructura de herencia de 3 niveles



# 2)
# incorporación de un método por cada clase creada



# 3)
# Pruebas para para comprobar la herencia de métodos y atributos.



# 4)
# Ejemplo de sobreescritura de método



# 5)
# Creación clase principal, para luego desarrollo de perfiles particulares



#  ----- Desarrollo -----










class cualquieraCosa():
    def __init__(self):
        pass
    def say(self):
        print('holaaaaaaa!!!!')


class algo(cualquieraCosa):
    def __init__(self):
        pass
    def say(self):
        print('aaaaaaaaaaa!!!!')



ejemplo1 = cualquieraCosa()
ejemplo2 = algo()


# ejemplo1.say()
ejemplo2.say()
