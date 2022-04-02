# m3-ABP4: OPCIÓN 2


print("\n---inicio del PROGRAMA---")
import random 
from random import sample
import time

# formularios
form = [
    "Cuestionario sobre Hábitos Alimenticios",
    "Cuestionario de Empleabilidad",
    "Cuestionario de Experiencia Laboral",
    "Cuestionario de Actividades Recreativas",
    "Cuestionario de Atletismo",
    "Cuestionario de Natación",
    "Cuestionario de Deportes en General"
]

form_sended = []
for user in range(7):
    num_of_form_to_send = random.randint(1, 5)
    temporalListForm = (sample(form,num_of_form_to_send))
    
    form_sended.append(num_of_form_to_send)
    # form_sended.append(num_of_form_to_send)

    print(f"\nEnvio a {num_of_form_to_send} formularios al usuario {user+1}")

    for e in temporalListForm:
        print(e)
        time.sleep(0.1) 

print("\nDatos finales\n")

n = 1
for i in form_sended:
    print(f"el usuario {n} repondió {i} formularios")
    n += 1

print("\n---Fin del PROGRAMA---\n")
