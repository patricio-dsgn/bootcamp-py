bodega = {'ZAPATILLAS': [20, 'PARES'],
              'POLERAS': [10, 'UNIDADES'],
              'ZAPATOS': [15, 'PARES'],
              'POLERÓN': [3, 'UNIDADES'],
              'CHAQUETA': [5, 'UNIDADES'],
              'GUANTES': [4, 'PARES']
              }

#mydict = {'george': 16, 'amber': 19}
#print(list(bodega.keys())[list(bodega.values()).index([20, 'PARES'])])

#hace una lista de las llaves del diccionario, las listas tienen index
#busca el index donde el valor de el diccionario es [20, 'PARES']

def Pato(diccionario, valores):
    '''#Se busca la posición de un valor --> (index de 26,ZAPATILLAs)
        #en la lista de valores  --> (list VALUES)
        #y luego con este número se elige
        #la posicion en la lista de keys --> (list KEYS)'''
    key = list(diccionario.keys())[list(diccionario.values()).index(valores)]
    print(key)

    return key

pato = Pato(bodega, [20, 'PARES'])