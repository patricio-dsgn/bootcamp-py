# Sprint Final del Módulo 3

_Acá va un párrafo que describa lo que es el proyecto_


_SPRINT DE ENTREGA_ 🚀


## 0. General

Este Sprint la implementación final de todos los conceptos vistos durante el Módulo 3 - Python básico.

El programa tiene tres partes:
1. manejo de bodega
2. información clientes
3. sistema de envío


## 1. Manejo de bodega

### Stock Productos:
- Datos de los productos: son vasos, cucharas, cuchillos y tenedores.
- Cada producto posee: un stock aleatorio entre 300 y 500 unidades
- Cada producto posee: una descripción

### Scripts:
- Crear y guardar la información de los productos en una bodega virtual.
- Sumar y disminuir el número de unidades por producto.
- Agregar nuevos productos.
- Quitar productos de la bodega virtual.
- Mostrar todos los productos disponibles y su stock. Debe tener un desfase de un segundo entre cada producto.
- Verificar si un producto tiene menos de 400 unidades y enviar una alerta.

### Funciones:
```

crearBodega()

alertaStock(stock)

mostarStock(bodega)

addElemento(
    bodega:dict,
    elemento: str,
    cantidad: int,
    descripcion: str
)

def removeElemento(
    bodega:dict,
    elemento: str,
    cantidad: int
)

```

## 2. Información clientes

### Clientes
- Datos: ID, nombre, apellido, edad y contraseña.
- Se han creado 4 clientes iniciales para probar el programa.
### Scripts:
- Crea una base de datos que tenga información de clientes.
- Agregar nuevos clientes.
- Eliminar clientes según ID.
- Mostrar toda la información por cliente.

### Funciones:
```

agregarClientes(
    clientes: dict,
    nombre: str,
    apellido: str,
    edad: int,
    contrasena: str
)

quitarClientes(
    clientes: dict,
    id: int
)

mostrarClientes(
    clientes: dict
)

```

## 3. Sistema de envío

### Condición rápido o largo:
- Si es un envío a una distancia de más de 1.000 km es considerado largo. Si es igual o menor a la distancia de 1.000 km es considerado rápido.

### Scripts:
- El sistema de envío pregunta qué tipo de envío es necesario (Rápido o largo)
- En el caso que sea un envío rápido se envía a una Bodega_A, caso contrario es almacenado a una Bodega_B.
- Verifica que cada bodega no supera las 500 unidades.

### Funciones:
```

crearBodega()

mostrarBodega(bodega_a, bodega_b)

comprobarCantidad(bodega)

agregarBodega(bodega_a, bodega_b)

```

## 4. ⌨️ Desarrollado por:

* Francisco Astete
* Ricardo Castillo
* Javier Espinoza
* Patricio Garrido
