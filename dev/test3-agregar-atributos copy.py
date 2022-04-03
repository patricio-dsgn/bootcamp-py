class User: 
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre



juan = User(234, 'juan perez')



juan.telefono = 968359053
# self.telefono = 968359053



# print(juan.telefono)



'''
__class__
__delattr__             delattr(Class, 'atribute')
__dict__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__                setattr(object, name, value)
__sizeof__
__str__
__subclasshook__
__weakref__
id
nombre
telefono

'''

class MyTest(object):

    def __init__(self, x):
        self.x = x

    def __setattr__(self, name, value):
        if name=="device":
            print("device test")
        else:
            super(MyTest, self).__setattr__(name, value)
            # in python3+ you can omit the arguments to super:
            #super().__setattr__(name, value)

MyTest