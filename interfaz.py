from tkinter import *
from tkinter import ttk

### buscar info sobre treeview  https://recursospython.com/guias-y-manuales/vista-de-arbol-treeview-en-tkinter/ ###

### Funciones ###

# Ventanas secundarias #


def ventana_secundaria(raiz, title, ancho=500, alto=500):
    nueva_ventana = Toplevel(raiz)
    nueva_ventana.title(title)
    nueva_ventana.config(width=ancho, height=alto)
    nueva_ventana.resizable(0, 0)
    nueva_ventana.grab_set()
    return nueva_ventana


def ventana_clientes():

    # Botones ventana Clientes #
    ventana = ventana_secundaria(
        ventana_principal, 'Clientes', ancho=622, alto=300)
    Button(ventana, text='Nuevo', width=10, height=2, font=(
        'bold', 10,), command=nuevo_cliente).place(x=10, y=10)
    Button(ventana, text='Buscar', width=10, height=2, font=(
        'bold', 10,), command=None).place(x=450, y=10)
    Entry(ventana, textvariable=StringVar).place(x=310, y=30)
    Label(ventana, text='Nombre :').place(x=250, y=30)
    mostrar_treeview(ventana, 10, 60, *('a', 'b'))
    return ventana


def nuevo_cliente():
    ventana = ventana_secundaria(
        ventana_principal, 'Nuevo cliente', ancho=200, alto=130)
    Label(ventana, text='Nombre :').place(x=10, y=10)
    Label(ventana, text='Telefono :').place(x=10, y=40)
    Entry(ventana, textvariable=StringVar).place(x=70, y=10)
    Entry(ventana, textvariable=IntVar).place(x=70, y=40)
    Button(ventana, text='Guardar', width=10, height=2, font=(
        'bold', 10,), command=None).place(x=60, y=70)
    return ventana


def ventana_stocks():
    return ventana_secundaria(ventana_principal, 'Stocks')


def ventana_pedidos():
    return ventana_secundaria(ventana_principal, 'Pedidos')


def ventana_ventas():
    return ventana_secundaria(ventana_principal, 'Ventas')


# Treeview #


def mostrar_treeview(raiz, eje_x=10, eje_y=10, *columnas):
    treeview = ttk.Treeview(raiz, columns=(columnas))
    treeview.place(x=eje_x, y=eje_y)
    return treeview


################## Se crea ventana principal, titulo y tamaño ##################

ventana_principal = Tk()
ventana_principal.title("Negocio 2024")
ventana_principal.config(width=440, height=70)
ventana_principal.resizable(0, 0)

################## Ventanas secundarias ##################

"""
Ventana con 4 botones
"""
# ventana_clientes = ventana_secundaria(ventana_principal, 'Clientes')
# ventana_stocks = ventana_secundaria(ventana_principal, 'Stocks')
# ventana_pedidos = ventana_secundaria(ventana_principal, 'Pedidos')
# ventana_ventas = ventana_secundaria(ventana_principal, 'Ventas')
#
################## Ventanas terciarias ##################

# Clientes #
"""
Nueva ventana con un listado de clientes y 3 botones 
"""
# nuevo_cliente = ventana_clientes = ventana_secundaria(
#    ventana_principal, 'Nuevo cliente')  # verificar si responde a la raiz o al toplevel.
# editar_cliente = ventana_clientes = ventana_secundaria(
#    ventana_principal, 'Editar cliente')
# buscar_cliente = ventana_clientes = ventana_secundaria(
#   ventana_principal, 'Buscar cliente')

# Stocks #
"""
Nueva ventana con un listado de stocks y 3 botones 
"""
# ingreso_stocks = ventana_secundaria(
#    ventana_principal, 'Nuevo ingreso')  # verificar si responde a la raiz o al toplevel.
# editar_stocks = ventana_secundaria(ventana_principal, 'Editar stocks')
# buscar_stocks = ventana_secundaria(ventana_principal, 'Buscar stocks')

# Pedidos #
"""
Nueva ventana con 3 botones 
"""
# nuevo_pedido = ventana_secundaria(
#    ventana_principal, 'Nuevo pedido')  # verificar si responde a la raiz o al toplevel.
# buscar_pedido = ventana_secundaria(ventana_principal, 'Buscar pedido')
# editar_pedido = ventana_secundaria(ventana_principal, 'Editar pedido')

# Ventas #
"""
Nueva ventana con un listado de ventas y 1 boton 
"""
# buscar_venta = ventana_secundaria(ventana_principal, 'Buscar ventas')

################## Labels (etiquetas de texto) ##################

# label = Label(ventana_principal, 'Texto')

################## Botones ventana principal ##################

## Determinar posicionamiento ##
# Botones principales

clientes = Button(ventana_principal, text='Clientes', width=10, height=2, font=('bold', 12,),
                  command=ventana_clientes).place(x=5, y=10)
stocks = Button(ventana_principal, text='Stocks', width=10, height=2, font=('bold', 12,),
                command=ventana_stocks).place(x=115, y=10)
pedidos = Button(ventana_principal, text='Pedidos', width=10, height=2, font=('bold', 12,),
                 command=ventana_pedidos).place(x=225, y=10)
ventas = Button(ventana_principal, text='Ventas', width=10, height=2, font=('bold', 12,),
                command=ventana_ventas).place(x=335, y=10)


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
ventana_principal.grab_set()
ventana_principal.mainloop()
