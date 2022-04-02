# DESARROLLO
# Como buen desarrollador, para comenzar a poder trabajar de manera óptima, es necesario que debamos
# preparar las herramientas necesarias para inicializar nuestro proyecto, esto incluye tener ya nuestro
# editor de texto y la versión de Python disponible en nuestro equipo.
# Familiarizado ya con estos componentes debemos prepararnos para realizar las siguientes acciones,
# para simular el funcionamiento de tu aplicación.


# ● Para desarrollar de mejor forma tu aplicación, requieres conocer mejor a los usuarios que la
# utilizarán. Antes de continuar desarrollando, debes elaborar un programa que tiene la funcionalidad de
# enviar cuestionarios a grupos particulares de personas.


# ● Los formularios varían según la edad, el lugar de origen y la afinidad con los deportes que tiene
# el usuario.


# ● El número máximo de cuestionarios a responder es de 3.


# ● Los usuarios que son originarios de América Latina responden el cuestionario sobre hábitos
# alimenticios.


# ● Los usuarios que NO son originarios de América Latina no responden el cuestionario de hábitos
# alimenticios.


# ● Todos los usuarios entre 18 y 29 años responden el cuestionario de empleabilidad. ok


# ● Los usuarios originarios de América Latina entre 30 y 59 años responden el cuestionario de   ok
# experiencia laboral.


# ● Los usuarios originarios de América Latina de 60 años y más responden el cuestionario de   ok
# actividades recreativas.


# ● Todos los usuarios que tienen afinidad por los deportes y que son menores de 60 años responden  ok
# el cuestionario de atletismo.


# ● Los usuarios originarios de América Latina que tienen afinidad por los deportes y que tienen 60   ok
# años o más responden el cuestionario de natación.


# ● Todos los usuarios que no tienen afinidad por los deportes responden un cuestionario de    ok
# Deportes en General.


# ● El usuario debe ingresar por consola sus características (lugar de origen, edad y afinidad por los
# deportes).


# ● Programa un mensaje que indique el número de cuestionarios a responder y cuáles son.

gentilicio = ['Belize', 'Costa Rica', 'El Salvador', 'Guatemala',
              'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Argentina', 'Bolivia',
              'Brazil', 'Chile', 'Colombia', 'Ecuador', 'French Guiana', 'Guyana',
              'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela',
              'Cuba', 'Dominican Republic', 'Haiti', 'Guadeloupe', 'Martinique',
              'Puerto Rico', 'Saint-Barthélemy', 'Saint-Martin']

gentilicio = [x.lower() for x in gentilicio]

while True:
    cuestionarios = []

    while True:
        edad = input('¿Cuál es tu edad? (numero)')
        if edad.isnumeric():
            break
        else:
            print('Debe ingresar su edad en numeros.')

    pais = input('¿Cuál es tu país de origen? ').lower()

    while True:
        afinidad = input('¿le gusta el deporte? ').lower()
        if afinidad in ['si', 'no']:
            break
        else:
            print('Debe ingresar si o no.')


    caracteristicas = {'lugar_origen': pais, 'edad': edad,
                       'afinidad_deporte': afinidad}

    if (int(caracteristicas['edad']) >= 1) and (caracteristicas['afinidad_deporte'] in ['si', 'no']):
        if caracteristicas['lugar_origen'] in gentilicio:
            # es de América Latina
            if (int(caracteristicas['edad']) >= 18) and (int(caracteristicas['edad']) <= 29):
                cuestionarios.append('empleabilidad')

            if (int(caracteristicas['edad']) >= 30) and (int(caracteristicas['edad']) <= 59):
                cuestionarios.append('experiencia laboral')

            if int(caracteristicas['edad']) >= 60:
                print('Debes responder el cuestionario de actividades recreativas')
                cuestionarios.append('actividades recreativas')

            if (caracteristicas['afinidad_deporte'] == 'si') and (int(caracteristicas['edad']) < 60):
                cuestionarios.append('atletismo')

            if (caracteristicas['afinidad_deporte'] == 'si') and (int(caracteristicas['edad']) >= 60):
                cuestionarios.append('natacion')

            if caracteristicas['afinidad_deporte'] == 'no':
                cuestionarios.append('Deportes en General')

            cuestionarios = cuestionarios[:3]
            print('Puedes responder los siguientes cuestionarios: ', cuestionarios)
            break

        else:
            # no es de América Latina. no se tiene lista del resto de paises.
            if (int(caracteristicas['edad']) >= 18) and (int(caracteristicas['edad']) <= 29):
                cuestionarios.append('empleabilidad')

            if (caracteristicas['afinidad_deporte'] == 'si') and (int(caracteristicas['edad']) < 60):
                cuestionarios.append('atletismo')

            if caracteristicas['afinidad_deporte'] == 'no':
                cuestionarios.append('Deportes en General')

            cuestionarios = cuestionarios[:3]
            print('Debes responder los siguientes cuestionarios: ', cuestionarios)
            break


    else:
        print('\nIngrese respuestas válidas')
        #break
