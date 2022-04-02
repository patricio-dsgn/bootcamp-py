productos = {
    'torta caramelo' : 1000,
    'galletas chocolate' : 600,
    'cake pop mermelada' : 400,
    'torta chocolate' : 700,
    'muffin de arándano': 500
}

demanda = {
    'torta caramelo' : 0,
    'galletas chocolate' : 0,
    'cake pop mermelada' : 0,
    'torta chocolate' : 0,
    'muffin de arándano' : 0
}

for key in demanda.keys():
    demanda[key] = input('¿cuantos '+key+' desea?')

cantidades = 0
for key in demanda.keys():
    cantidades = cantidades + (int(demanda[key]) * productos[key]) 

cantidades_iva = cantidades * 1.19

print('El total neto: '+str(cantidades))
print('El total de la venta es: '+str(cantidades_iva))
