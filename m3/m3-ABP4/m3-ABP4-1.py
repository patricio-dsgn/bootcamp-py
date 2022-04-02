# m3-ABP4: OPCIÓN 1

print("\n---inicio del PROGRAMA---\n")


print("\nREGISTRO DE USUARIO\n")
u = input('registre su usuario: ')
# contraseñas para testear
# p = '12345678'
# p = 'abcdefgh'
# p = 'AaAaAaAaAaAa23'
cont_digit = 0
cont_alpha = 0
cont_lower = 0
cont_upper = 0


flag = 0
while(flag == 0):
    p = input('registre su contraseña: ')

    for char in p:
        if char.isdigit(): cont_digit += 1
        if char.isalpha(): cont_alpha += 1
        if char.islower(): cont_lower += 1
        if char.isupper(): cont_upper += 1

    if(
        len(p)>=8 and # largos de 8 carácteres
        cont_lower != 0 and # incluir mayúsculas
        cont_upper != 0 and # incluir minúsculas
        cont_digit != 0 and # incluir números
        cont_alpha != 0 # incluir letras
    ):
        flag += 1
        break

    else:
        print("--contraseña no segura--")

print("contraseña OK!")


print("\n---Fin del PROGRAMA---\n")



