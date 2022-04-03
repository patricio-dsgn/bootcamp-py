from prompt_toolkit import print_formatted_text


productos= {
    'prod1':{"Zapatillas": 20,},
    'prod2':{"Poleras": 10, },
    'prod3':{"Zapatos": 15, },
    'prod4':{"Poleron": 3, },
    'prod5':{"Chaquetas": 5, },
    'prod6':{"Guantes": 4}
}


def checking_products(x):
    for product, info in x.items():
        # print(info)
        #Iterate the items in the nested dictionary.
        for key in info.keys():
            print(f'Producto:{key}, id: {product} = {info[key]} unidades')
            # print(key)
            # print(product)
            # print(info[key])
    return x




def add_products():
    while True:
        add_id=input('Ingrese ID del producto ( Formato: prod(num)=prod6 ): ')
        add_prod=input('Ingrese nuevo producto: ').capitalize()
        add_units=input('Ingrese número de unidades (sólo digitos): ')
        #Display on screen added product and respective value.
        if add_prod in productos.keys():
            productos[add_prod]=productos[add_prod]+add_units
            print(f'Producto {add_prod} actualizado exitosamente: {add_prod}: {productos[add_prod]} unidades')
        elif add_prod not in productos:        
            productos[add_id][add_prod]=add_units
            print(f'Producto {add_prod} agregado exitosamente: {add_prod}: {add_units} unidades')
        if storage_complete():
            # Takes us out of the function.
            return 

def storage_complete():
# """problema: no funciona el "No"""
    answer = input("Desea agregar otro producto a bodega?: ").capitalize
    if answer == "No":
        return True
    elif answer == "Sí" or "Si":
        return False
    else:
        print("Respuesta inválida")

#Display and return the available/updated units per product.
def update_warehouse(storage_list):
    print(f'Bodega actualizada con nuevos productos: ' )
    #Go through each value in the data structure (dict), assign the value to a variable, and perform logic on each one individually.
    for product in storage_list:
        print(f"{product}: {storage_list[product]}")


def main():
    store= add_products()
    update_warehouse(store)
    print("Almacenaje Completado Exitosamente.")



#Display and return an specific product in the store.
def specific_product():
    product= input('Ingrese el producto que desea revisar: ').capitalize()
    if product in productos.keys():
        print(f'Disponemos de {productos[product]} unidades de {product}')
        return
    elif product not in productos.keys():
        print(f'Lo sentimos. Actualmente no contamos con {product}.')
        return product

#Display and return all products in the store.
def whole_warehouse ():  
    print('Actualmente contamos con los siguientes productos:')
    for key in productos.keys():
        print(f"{key}: {productos[key]}")
    return



#Dispaly and return products requested by the customer that have a certain number of units.
def product_by_num():
    requested_prod=int(input('Ingrese unidades que necesita (sólo digitos): '))
    #Go through each value in the data structure (dict).
    for key in productos.keys():
        if requested_prod >= productos[key]:
            print(f'Lo sentimos. Ninguno de nuestros productos tiene el stock que usted requiere.')    
        else:
            # print(f'Los productos que contienen dicha cantidad son:')
            """ problema: imprime solo 1 """
            print(f'{key}: {productos[key]}')  
            return 




# checking_products(productos)
add_products()
# storage_complete()
# update_warehouse(storage_list)


# specific_product()
# whole_warehouse () 
# product_by_num()
