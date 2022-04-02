# m3-ABP5



# 7 diccionarios para 7 usuarios
user0 ={
	'Primer Nombre': 'Andrés',
	'Segundo Nombre': 'Alberto',
	'Apellido Paterno': 'Alvares',
	'Apellido Materno': 'Ávila',
	'Edad' : 37,
	'Domicilio' : 'Calle 10 # 5-51',
	'Telefóno' : 968650311,
	'Correo electrónico' : 'andres34@mail.com',
	'Actividad laboral' : 'Diseñador',
	'RUT' : '15777822-5'
}

user1 ={
	'Primer Nombre': 'Begoña',
	'Segundo Nombre': 'Bruna',
	'Apellido Paterno': 'Benavides',
	'Apellido Materno': 'Bravo',
	'Edad' : 35,
	'Domicilio' : 'Calle 53 No 10-60/46, Piso 2',
	'Telefóno' : 922653377,
	'Correo electrónico' : 'begonia12@mail.com',
	'Actividad laboral' : 'Peluquera',
	'RUT' : '16267822-5'
}

user2 ={
	'Primer Nombre': 'Catalina',
	'Segundo Nombre': 'Camila',
	'Apellido Paterno': 'Cortés',
	'Apellido Materno': 'Cuevas',
	'Edad' : 42,
	'Domicilio' : 'Carrera 21 # 17 - 63',
	'Telefóno' : 961250312,
	'Correo electrónico' : 'catalina99@mail.com',
	'Actividad laboral' : 'Profesora',
	'RUT' : '13722821-3'
}

user3 ={
	'Primer Nombre': 'Dario',
	'Segundo Nombre': 'David',
	'Apellido Paterno': 'Dubois',
	'Apellido Materno': 'Dupont',
	'Edad' : 38,
	'Domicilio' : 'Carrera 11 # 41-13',
	'Telefóno' : 913350333,
	'Correo electrónico' : 'dario0@mail.com',
	'Actividad laboral' : 'Poeta',
	'RUT' : '15000111-k'
}

user4 ={
	'Primer Nombre': 'Eva',
	'Segundo Nombre': 'Edith',
	'Apellido Paterno': 'Echebarría',
	'Apellido Materno': 'Estrada',
	'Edad' : 30,
	'Domicilio' : 'Avenida 1 # 28-57',
	'Telefóno' : 961150117,
	'Correo electrónico' : 'eva01@mail.com',
	'Actividad laboral' : 'Actriz',
	'RUT' : '20111022-2'
}

user5 ={
	'Primer Nombre': 'Facundo',
	'Segundo Nombre': 'Fernando',
	'Apellido Paterno': 'Fernandez',
	'Apellido Materno': 'Flores',
	'Edad' : 33,
	'Domicilio' : 'Calle 100 # 11B-27',
	'Telefóno' : 928610117,
	'Correo electrónico' : 'facundo11@mail.com',
	'Actividad laboral' : 'Arquitecto',
	'RUT' : '17123000-5'
}

user6 ={
	'Primer Nombre': 'Gabriela',
	'Segundo Nombre': 'Gertrudis',
	'Apellido Paterno': 'Goméz',
	'Apellido Materno': 'González',
	'Edad' : 23,
	'Domicilio' : 'Calle 23 #127',
	'Telefóno' : 933610123,
	'Correo electrónico' : 'gaby11@mail.com',
	'Actividad laboral' : 'Cantante',
	'RUT' : '27123000-1'
}

#union de los 7 diccionarios en una lista
users = [
	user0,
	user1,
	user2,
	user3,
	user4,
	user5,
	user6
]


#Título (dibujito en la consola)
print(
	"\n"
	"\n|- - - - - - - - - - - - - - - - - - - -|"
	"\n| 7 Diccionarios unidos en una lista    |"
	"\n|                                       |"
	"\n| users = [                             |"
	"\n|       user0,                          |"
	"\n|       user1,                          |"
	"\n|       user2,                          |"
	"\n|       user3,                          |"
	"\n|       user4,                          |"
	"\n|       user5,                          |"
	"\n|       user6,                          |"
	"\n|       user7                           |"
	"\n| ]                                     |"
	"\n|- - - - - - - - - - - - - - - - - - - -|\n"
)

#imprimir cada dato
for x in users:
	print (
		x["Primer Nombre"]
		+' '+x["Segundo Nombre"]
		+' '+x["Apellido Paterno"]
		+' '+x["Apellido Materno"]+"\n"
		+str(x['Edad'])+' años'+"\n"
		+"dir: "+ x['Domicilio']+"\n"
		+"fono: "+ str(x['Telefóno'])+"\n"
		+"mail: "+ x['Correo electrónico']+"\n"
		+"act: "+ x['Actividad laboral']+"\n"
		+"rut: "+ x['RUT']
		+"\n"
	)








# ¿Qué problemas encontró con esta forma de almacenar la información?
#  tuve que codear mucho y no es escalable


# estructura de datos unificada
# + nombre_usuario
# + id_unico
# + antigüedad
# + fecha de incorporación


db = [
	[{
		'id' : 'user1',
		'user' : 'Andrés',
		'Antigüedad': '503 días',
		'Incorporación': '10,10,2020',
		'Primer Nombre': 'Andrés',
		'Segundo Nombre': 'Alberto',
		'Apellido Paterno': 'Alvares',
		'Apellido Materno': 'Ávila',
		'Edad' : 37,
		'Domicilio' : 'Calle 10 # 5-51',
		'Telefóno' : 968650311,
		'Correo electrónico' : 'andres34@mail.com',
		'Actividad laboral' : 'Diseñador',
		'RUT' : '15777822-5'
	}],[{
		'id' : 'user2',
		'user' : 'Begoña',
		'Antigüedad': '368 días',
		'Incorporación': '22,2,2021',
		'Primer Nombre': 'Begoña',
		'Segundo Nombre': 'Bruna',
		'Apellido Paterno': 'Benavides',
		'Apellido Materno': 'Bravo',
		'Edad' : 35,
		'Domicilio' : 'Calle 53 No 10-60/46, Piso 2',
		'Telefóno' : 922653377,
		'Correo electrónico' : 'begonia12@mail.com',
		'Actividad laboral' : 'Peluquera',
		'RUT' : '16267822-5'
	}],[{
		'id' : 'user3',
		'user' : 'Catalina',
		'Antigüedad': '299 días',
		'Incorporación': '2,5,2021',
		'Primer Nombre': 'Catalina',
		'Segundo Nombre': 'Camila',
		'Apellido Paterno': 'Cortés',
		'Apellido Materno': 'Cuevas',
		'Edad' : 42,
		'Domicilio' : 'Carrera 21 # 17 - 63',
		'Telefóno' : 961250312,
		'Correo electrónico' : 'catalina99@mail.com',
		'Actividad laboral' : 'Profesora',
		'RUT' : '13722821-3'
	}],[{
		'id' : 'user4',
		'user' : 'Dario',
		'Antigüedad': '268 días',
		'Incorporación': '2,6,2021',
		'Primer Nombre': 'Dario',
		'Segundo Nombre': 'David',
		'Apellido Paterno': 'Dubois',
		'Apellido Materno': 'Dupont',
		'Edad' : 38,
		'Domicilio' : 'Carrera 11 # 41-13',
		'Telefóno' : 913350333,
		'Correo electrónico' : 'dario0@mail.com',
		'Actividad laboral' : 'Poeta',
		'RUT' : '15000111-k'
	}],[{
		'id' : 'user5',
		'user' : 'Eva',
		'Antigüedad': '196 días',
		'Incorporación': '13,8,2021',
		'Primer Nombre': 'Eva',
		'Segundo Nombre': 'Edith',
		'Apellido Paterno': 'Echebarría',
		'Apellido Materno': 'Estrada',
		'Edad' : 30,
		'Domicilio' : 'Avenida 1 # 28-57',
		'Telefóno' : 961150117,
		'Correo electrónico' : 'eva01@mail.com',
		'Actividad laboral' : 'Actriz',
		'RUT' : '20111022-2'
	}],[{
		'id' : 'user6',
		'user' : 'Facundo',
		'Antigüedad': '166 días',
		'Incorporación': '12,9,2021',
		'Primer Nombre': 'Facundo',
		'Segundo Nombre': 'Fernando',
		'Apellido Paterno': 'Fernandez',
		'Apellido Materno': 'Flores',
		'Edad' : 33,
		'Domicilio' : 'Calle 100 # 11B-27',
		'Telefóno' : 928610117,
		'Correo electrónico' : 'facundo11@mail.com',
		'Actividad laboral' : 'Arquitecto',
		'RUT' : '17123000-5'
	}],[{
		'id' : 'user6',
		'user' : 'ger',
		'Antigüedad': '31 días',
		'Incorporación': '25,1,2022',
		'Primer Nombre': 'Gabriela',
		'Segundo Nombre': 'Gertrudis',
		'Apellido Paterno': 'Goméz',
		'Apellido Materno': 'González',
		'Edad' : 23,
		'Domicilio' : 'Calle 23 127',
		'Telefóno' : 933610123,
		'Correo electrónico' : 'gaby11@mail.com',
		'Actividad laboral' : 'Cantante',
		'RUT' : '27123000-1'
	}]
]





#Título (dibujito en la consola)
print(
	"\n"
	"\n|- - - - - - - - - - - - - - - - - - - -|"
	"\n| Estructura de datos unificada de      |"
	"\n| muchos dic dentro de en una lista     |"
	"\n|                                       |"
	"\n| bd = [                                |"
	"\n|       [{}],                           |"
	"\n|       [{}],                           |"
	"\n|       [{}],                           |"
	"\n|       [{}],                           |"
	"\n|       [{}],                           |"
	"\n|       [{}],                           |"
	"\n|       [{}],                           |"
	"\n|       [{}],                           |"
	"\n|       [{}],                           |"
	"\n| ]                                     |"
	"\n|- - - - - - - - - - - - - - - - - - - -|\n"
)


pos = 0
for x in db:

	print(
		"pos: "+ str(pos)+"\n"
		+"id: "+x[0]["id"]+"\n"
		+"user: "+x[0]["user"]+"\n"
		+"anti: "+x[0]["Antigüedad"]+"\n"
		+"inco: "+x[0]["Incorporación"]+"\n"

		+''+x[0]["Primer Nombre"]
		+' '+x[0]["Segundo Nombre"]
		+' '+x[0]["Apellido Paterno"]
		+' '+x[0]["Apellido Materno"]+"\n"

		+str(x[0]['Edad'])+' años'+"\n"

		+"dir: "+ x[0]['Domicilio']+"\n"
		+"fono: "+ str(x[0]['Telefóno'])+"\n"
		+"mail: "+ x[0]['Correo electrónico']+"\n"

		+"act: "+ x[0]['Actividad laboral']+"\n"
		+"rut: "+ x[0]['RUT']

		+"\n"
	)

	pos += 1