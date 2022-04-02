# m3-ABP2

# Instrucciones
# Clave para acceso restringido es: 1234
# Los nombres que se pueden buscar son:
# Andres, Bruno, Cecilia, Dania, Ester, Felipe, Godinez






print("\n")
print("---inicio del PROGRAMA---")

# Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce
# Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
# Convierte tu string en una lista, en la cual cada elemento es un usuario.
cadena = 'Andres,Bruno,Cecilia,Dania,Ester,Felipe,Godinez'
matriz = cadena.split(',')

# ● Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.
print("\n")
print(f"La posición de Bruno en la lista es: {matriz.index('Bruno')}")
print(f"La posición de Dania en la lista es: {matriz.index('Dania')}")
print(f"La posición de Godinez en la lista es: {matriz.index('Godinez')}")
print("\n")



# ● ¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente su nombre? ¿Cómo solucionarías este problema?
k = input("Acceso restringido, ingresa clave: ")
if(k=='1234'):
	f = input("Búsca un usuario: ").title()
	flag = 0
	for i in matriz:
		if f == i:
			print(f"\n*** {f} existe en lista ***\n")
			flag += 1
	
	if flag == 0:
		print(f"\n*** {f} NO existe en lista ***\n")


	# Imprima en pantalla la cantidad usuarios que tiene tu aplicación.
	print(f"Cantidad usuarios que tiene la aplicación: {len(matriz)}\n")

	# Imprima en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes utilizar para realizar esto?
	for i in matriz:
		print(f"Que tengas un buen día {i}, Saludos.")
	print("\n")


else:
	print(f"\nno tienes acceso :(\n")


print("---Fin del PROGRAMA---\n")





