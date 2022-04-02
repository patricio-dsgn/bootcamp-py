

# Generalization
# ----------------------------------------------------------------

class Robot:
    def __init__(self, name):
        self.name = name

    def walk(self,direction):
        print(f"\033[1;32mwalk to {direction}\033[0;37m")

class Robot_de_servicio(Robot):
    def __init__(self, name, services):
        super().__init__(name)
        self.services = services

    def hello(self, mesage):
        print(f"\033[3;33m{mesage}\033[0;37m")






# Realization/Implementation
# ----------------------------------------------------------------
vending_machine_1  = Robot_de_servicio('vm123','candy machine')


vending_machine_1.hello('buenos dias, estimado cliente')