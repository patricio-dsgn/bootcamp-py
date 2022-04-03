# m3-ABP6
import time


def printy(x,arr):
	if x == 'start': print("\n---inicio del PROGRAMA---\n")
	elif x == 'end': print("\n---Fin del PROGRAMA---\n")
	elif x == 'full_list':
		print("\nlista completa\nUSUARIO / CONTRASEÑA / EDAD")
		for i in arr:
			print(f"{i[0]} / {i[1]} / {i[2]}")
			time.sleep(5)
		print("\n")


def inputy(txt):
	out = 'salir'; val = ''
	while (val == '' or val != out): val = input(txt)
	return val


def valy(n,arr):
	name = inputy('ingresa tu nombre: ')
	password = inputy('ingresa tu contraseña: ')
	age = input('ingresa tu edad: ')
	arr.append([name,password,age])
	n += 1
	return arr

def app():
	n = 0
	arr = []
	printy("start",arr)
	arr = valy(n,arr)
	printy("full_list",arr)
	printy("end",arr)

app()