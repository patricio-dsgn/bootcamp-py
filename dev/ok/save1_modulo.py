import json


class Save:

    @classmethod
    def saving(self, file):
        # leer .json, JSON a python (convertir formato datos)
        with open(file) as json_file:
            data = json.load(json_file)



        # agregar nuevos datos
        pregunta = input("deseas agregar algo? si/no: ")
        if pregunta == 'si':
            k = input("id: ")
            n = input("nombre: ")
            m = input("mail: ")
            data[k] = [n, m]
        else:
            print('no agregaste nada')


        # borrar datos
        pregunta = input("deseas borrar? si/no: ")
        if pregunta == 'si':
            key = input("que clave quiere borrar?")
            del data[key]

        else:
            print('no borras nada')

        # print(data)
        # python a JSON (convertir formato datos)
        json_object = json.dumps(data, indent = 4) 


        # abrir .json, escribir, cerrar
        f = open("data.json", "w")
        f.write(json_object)

