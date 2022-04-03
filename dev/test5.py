
class A:
    def __init__(self):
        self.uno = 1

class B:
    dos = 2

class C:
    tres = 3

class All(A,B,C):
    pass


a = All()

# print(a.uno)
# print(a.dos)
print(a.tres)




# class A: pass


# a = A()
# b = A()


# print(hex(id(a)))
# print(hex(id(b)))