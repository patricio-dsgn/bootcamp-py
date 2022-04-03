
class Marifer:

    @classmethod
    def veri_1(self,cosa_a, cosa_b):
        print(cosa_a, cosa_b)

    @classmethod
    def veri_2(self,a):
        x = input(a)
        return x


# método 1
Marifer.veri_1('arbol','perro')


# método 2
test = Marifer.veri_2('escribe algo Alimal!: ')
print(test)