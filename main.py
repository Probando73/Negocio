import clase_bd
import interfaz as gui
from tkinter import *
from tkinter import ttk

if __name__ == "__main__":

    # Diccionarios con los nombres de las tablas y tipo de campo.
    tabla_clientes = {
        'ID': 'INTEGER  AUTO_INCREMENT PRIMARY KEY',
        'Cliente': 'TEXT NOT NULL',
        'Telefono': 'INTEGER NOT NULL',
    }

    tabla_ventas = {
        'N° Pedido': 'INTEGER AUTO_INCREMENT PRIMARY KEY',
        'Cliente': 'TEXT NOT NULL ',
        'Cant_Productos': 'INTEGER NOT NULL',
        'Monto': 'INTEGER NOT NULL',
    }

    tabla_pedidos = {
        'ID': 'INTEGER AUTO_INCREMENT ',
        'N° Pedido': 'INTEGER PRIMARY KEY',
        'Cliente': 'TEXT NOT NULL',
        'Marca': 'TEXT NOT NULL',
        'Producto': 'TEXT NOT NULL',
        'Cantidad': 'INTEGER NOT NULL',
        'Precio_unitario': 'INTEGER NOT NULL',
        'Subtotal': 'INTEGER NOT NULL',
    }

    tabla_stocks = {
        'ID': 'INTEGER  AUTO_INCREMENT',
        'Marca': 'TEXT NOT NULL',
        'Producto': 'TEXT  NOT NULL PRIMARY KEY',
        'Cantidad': 'INTEGER NOT NULL',
        'Precio_mercado': 'INTEGER NOT NULL',
        'Precio_de_venta': 'INTEGER NOT NULL',
    }
"""
    # Se crea la base de datos principal.
    base_datos = clase_bd.BBDD("Negocio_2024")

    # Se crean las tablas en la BBDD
    clientes = base_datos.create_table("clientes", **tabla_clientes)

    ventas = base_datos.create_table("ventas",
                                     Fk='Cliente',
                                     References_table='clientes',
                                     references_field='ID',
                                     **tabla_ventas)

    pedidos = base_datos.create_table("pedidos",
                                      Fk='N° Pedido',
                                      References_table='ventas',
                                      references_field='N° Pedido',
                                      **tabla_pedidos)

    stocks = base_datos.create_table("stocks",
                                     Fk='Precio_de_venta',
                                     References_table='pedidos',
                                     references_field='Precio_unitario',
                                     **tabla_stocks)

    # Se crean los registros a guardar

    datos_clientes = [
        ('Maximiliano', 1156236548),
        ('Juan', 1156243548),
        ('Maria', 1156243548),
        ('Jose', 1156243548),
    ]

    datos_stocks = [
        ('Sedal', 'Acondicionador 650 ml', 24, 1300, 2000),
        ('Sedal', 'Acondicionador 950 ml', 24, 1300, 2000),
        ('Sedal', 'Acondicionador 1250 ml', 24, 1300, 2000),
        ('Sedal', 'Acondicionador 1500 ml', 24, 1300, 2000),
    ]

    # Inserto los datos creados en la tabla clientes

    base_datos.insert_more('clientes', *datos_clientes)
    base_datos.insert_more('stocks', *datos_stocks)
    print(base_datos.read('clientes'))

    base_datos.update_where('clientes', 'Telefono', 800,
                            'Cliente', '=', 'Maximiliano')
    print(base_datos.read('clientes'))

    # base_datos.delete_where('clientes', 'Cliente', '=', 'Juan')
    print(base_datos.read('clientes'))

    ################## Se crea ventana principal, titulo y tamaño ##################


################## Ventanas secundarias ##################


# Pedidos #
"""
# Nueva ventana con 3 botones
"""
# nuevo_pedido = ventana_secundaria(
#    ventana_principal, 'Nuevo pedido')  # verificar si responde a la raiz o al toplevel.
# buscar_pedido = ventana_secundaria(ventana_principal, 'Buscar pedido')
# editar_pedido = ventana_secundaria(ventana_principal, 'Editar pedido')

# Ventas #
"""
# Nueva ventana con un listado de ventas y 1 boton
"""
# buscar_venta = ventana_secundaria(ventana_principal, 'Buscar ventas')

#### instancio la clase ventana ###

"""
ventana_principal = gui.Ventana()
"""
################## Botones ventana principal ##################

## Determinar posicionamiento ##
# Botones principales


# Botones ventana Stocks #

# stocks_nuevo = Button(ventana_principal, text='Nuevo', command=ingreso_stocks)
# stocks_editar = Button(ventana_principal, text='Editar', command=editar_stocks)
# stocks_buscar = Button(ventana_principal, text='Buscar', command=buscar_stocks)

# Botones ventana Pedidos #

# pedidos_nuevo = Button(ventana_principal, text='Nuevo', command=nuevo_pedido)
# pedidos_editar = Button(
#    ventana_principal, text='Editar', command=editar_pedido)
# pedidos_buscar = Button(
#    ventana_principal, text='Buscar', command=buscar_pedido)

# Botones ventana Ventas #

# ventas_buscar = Button(ventana_principal, text='Nuevo', command=buscar_venta)

"""
