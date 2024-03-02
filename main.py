import clase_bd
import interfaz as gui
from tkinter import *
from tkinter import ttk

if __name__ == "__main__":

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



#### instancio la clase ventana ###

ventana_principal = gui.Ventana()
