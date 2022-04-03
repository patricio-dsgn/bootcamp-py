# m3-ABP6
import time



#  - - - - - - - - - - - - - 
# |       funciones         |
#  - - - - - - - - - - - - - 


# funcion para imprimir comentarios
def printy(x,arr):
	if x == 'start': print("\n---inicio del PROGRAMA---\n")
	elif x == 'end': print("\n---Fin del PROGRAMA---\n")
	elif x == 'full_list':
		print("\nlista completa\nUSUARIO / CONTRASEÑA / EDAD")
		for i in arr:
			print(f"{i[0]} / {i[1]} / {i[2]}")
			time.sleep(5)
		print("\n")



# funcion para validar entradas correctas en input
def valy(n,arr):
	out = 'salir'
	while (True):
		name = input('ingresa tu nombre: ')
		if(name == out): break

		password = input('ingresa tu contraseña: ')
		if(password == out): break

		while (True):
			age = input('ingresa tu edad: ')
			if(age.isdecimal()): break
			if(age == out): break
		if(age == out): break
		
		arr.append([name,password,age])
		n += 1

	return arr



# funcion general para ordenar el flujo
def app():
	n = 0; arr = []
	printy("start",arr)
	arr = valy(n,arr)
	printy("full_list",arr)
	printy("end",arr)


#  - - - - - - - - - - - - - 
# |     Implementación      |
#  - - - - - - - - - - - - - 

app()