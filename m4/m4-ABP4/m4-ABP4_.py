# ABP4
 
 

#  ----- Documentación -----



# 1)
# Integración de una estructura de herencia de 3 niveles



# 2) 
# Comprobación de la herencia de métodos y atributos



# 3)
# Creación de una clase principal: User



# 4)
# Uso de ORM orden de resolución de métodos.



# 5)
# Utilidad del polimorfismo en la definición de métodos heredados



# 6)
# isinstance()
# Indique en qué momento es conveniente utilizar las 
# funciones 



# 7)
# y issubclass()



#  ----- Desarrollo -----


class Arbol():
    pass

class Olivo(Arbol):
    pass

# print(issubclass(Olivo,Arbol))


arbol1 = Arbol()
arbol2 = Olivo()

print(isinstance(arbol1,Arbol))





class A: 
    def rk(self): 
        print(" In class A") 
class B: 
    def rk(self): 
        print(" In class B") 
  
class C(A, B): 
    def __init__(self): 
        print("Constructor C") 
  
r = C() 
  
print(C.__mro__) 
print(C.mro())


