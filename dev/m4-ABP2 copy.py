# ABP2



#  ----- Documentación -----



# 1)
# Incorporación nueva clase
# REPARTIDOR



# 2)
# Incorporación atributos y métodos

# ADMINISTRADOR
# Atributos: lista clientes, lista asistentes, datos servidor, catálogo
# Acciones: ver usuarios, agregar usuario, quitar usuario, bloquear tienda

# ASISTENTE
# Atributos: lista clientes, libro de preguntas, libro de notas, catálogo
# Acciones: ver preguntas, responder pregunta, crear nota, borrar nota

# CLIENTE
# Atributos: dirección, historial, carro de compra, catálogo
# Acciones: elegir producto, pagar producto, hacer pregunta, buscar producto

# REPARTIDOR
# Atributos: Envios realizados, Envios pendientes, Vehículo, Horario(opcional)
# Acciones: Ubicación, Kilometros recorridos, Capacidad diponible, Alerta de problema en entrega


# 3)
# Diagrama Adjunto: m4-ABP2.jpg

# NOTA 1: los metodos incluyen 2 acciones que afecten números y 2 que afecten strings
# NOTA 2: se ha aplicado 'sobrecarga de métodos' con válidaciones.



#  ----- Desarrollo -----

class Delivery():
# Atributos: Envios realizados, Envios pendientes, Vehículo, Horario(opcional)
# Acciones: Ubicación, Kilometros recorridos, Capacidad diponible, Alerta de problema en entrega

    def __init__(self, shipments_ready, pending_shipments, vehicle, schedule):
        self.shipments_ready = shipments_ready
        self.pending_shipments = pending_shipments
        self.vehicle = vehicle
        self.schedule = schedule

    def location(self):
        for x in self.clients:
            print(x)

    def kilometers(self):
        for x in self.asistants:
            print(x)

    def available_capacity(self):
        for x in self.data_server:
            print(x)

    def delivery_problem_alert(self):
        for x in self.data_server:
            print(x)














# class delivery():
#     pass


# class Promo:
#     def __init__(self, points=None, person_two=None):
#         if person_one is not None and person_two is None:
#             print("Hi, " + person_one)
#         elif person_one is not None and person_two is not None:
#             print("Hi, " + person_one + " and " + person_two)
#         else: 
#             print("Who's there? ")

# DefObj = Home()

# DefObj.Knock()
# DefObj.Knock('Rick','Morty','32424')
# DefObj.Knock('Sam')

