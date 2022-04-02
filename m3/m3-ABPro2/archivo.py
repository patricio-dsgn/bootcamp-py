#i. A una variable se le asigne un mensaje motivador que incluya los nombres de todos los
#integrantes. ¿Qué tipo de dato puede ser?

mensaje = "Compra con nosotros, empresa desarrollada por Patricio, Francisco, Ricardo y Javier" 
#print(mensaje) 

#ii. Se asegure que todos su caracteres estén en mayúscula.

mensaje=mensaje.upper()
#print(mensaje)

#iii. Elabore una lista con cada palabra del string.

mensaje=mensaje.replace(",","")
lista_mensaje=mensaje.split()
#print(lista_mensaje)

#iv. Cada integrante del grupo debe reconocer en qué índice está su nombre.


for integrante in ["Ricardo","patricio","FRANcIsCO","JAviER"]:
    print(f"index {integrante.upper()} es {lista_mensaje.index(integrante.upper())}")

#v. Indique cuántas palabras tenía el string.

print(f"la frase tiene {len(lista_mensaje)} palabras")

#vi. Imprima una tupla con todas las palabras del string.

tupla_mensaje=tuple(lista_mensaje)
print(tupla_mensaje)

#vii. ¿Con qué función podrían obtener el mensaje por teclado al ejecutar el programa? Implementarlo!.

while True:
    respuesta=input("quieres un mensaje motivador? si/no").lower()
    if respuesta=="si":
        print(mensaje)
        break
    if respuesta=="no":
        print("que pena")
        break
    else:
        print("ingrese una respuesta valida (si/no)")





