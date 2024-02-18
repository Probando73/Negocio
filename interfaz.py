from tkinter import *  
from tkinter import tkk

### buscar info sobre treeview  https://recursospython.com/guias-y-manuales/vista-de-arbol-treeview-en-tkinter/ ###

### Funciones ###

# Ventanas secundarias #
def ventana_secundaria(raiz, title):
    nueva_ventana = Toplevel(raiz)
    nueva_ventana.title(title)
    nueva_ventana.config(width=500, height=500)
    return nueva_ventana

# Treeview #
def mostrar_treeview(raiz, *columnas):
    treeview = ttk.Treeview(raiz, columns= (columnas))
    treeview.pack()
    return treeview
    
    
################## Se crea ventana principal, titulo y tamaño ##################

ventana_principal = Tk()
ventana_principal.title("Negocio 2024")
ventana_principal.config(width=500, height=500)

################## Ventanas secundarias ##################

"""
Ventana con 4 botones
"""
ventana_clientes = ventana_secundaria(ventana_principal, 'Clientes')
ventana_stocks = ventana_secundaria(ventana_principal, 'Stocks')
ventana_pedidos = ventana_secundaria(ventana_principal, 'Pedidos')
ventana_ventas = ventana_secundaria(ventana_principal, 'Ventas')

################## Ventanas terciarias ##################

# Clientes #
"""
Nueva ventana con un listado de clientes y 3 botones 
"""
nuevo_cliente = ventana_clientes = ventana_secundaria(ventana_principal, 'Nuevo cliente') # verificar si responde a la raiz o al toplevel.
editar_cliente = ventana_clientes = ventana_secundaria(ventana_principal, 'Editar cliente')
buscar_cliente = ventana_clientes = ventana_secundaria(ventana_principal, 'Buscar cliente')

# Stocks #
"""
Nueva ventana con un listado de stocks y 3 botones 
"""
ingreso_stocks = ventana_secundaria(ventana_principal, 'Nuevo ingreso') # verificar si responde a la raiz o al toplevel.
editar_stocks = ventana_secundaria(ventana_principal, 'Editar stocks')
buscar_stocks =  ventana_secundaria(ventana_principal, 'Buscar stocks')

# Pedidos #
"""
Nueva ventana con 3 botones 
"""
nuevo_pedido = ventana_secundaria(ventana_principal, 'Nuevo pedido') # verificar si responde a la raiz o al toplevel.
buscar_pedido = ventana_secundaria(ventana_principal, 'Buscar pedido') 
editar_pedido = ventana_secundaria(ventana_principal, 'Editar pedido')

# Ventas #
"""
Nueva ventana con un listado de ventas y 1 boton 
"""
buscar_venta = ventana_secundaria(ventana_principal, 'Buscar ventas')

################## Labels (etiquetas de texto) ##################

label = Label(ventana_principal, 'Texto')

################## Botones ventana principal ##################

## Determinar posicionamiento ## 
# Botones principales #

clientes = Button(ventana_principal, text= 'Clientes', command= ventana_clientes)
stocks = Button(ventana_principal, text= 'Stocks', command= ventana_stocks)
pedidos = Button(ventana_principal, text= 'Pedidos', command= ventana_pedidos)
ventas = Button(ventana_principal, text= 'Ventas', command= ventana_ventas)

# Botones ventana Clientes #

cliente_nuevo = Button(ventana_principal, text= 'Nuevo', command= nuevo_cliente)
cliente_editar = Button(ventana_principal, text= 'Editar', command= editar_cliente)
cliente_actualizar = Button(ventana_principal, text= 'Actualizar', command= actualizar_cliente)

# Botones ventana Stocks #

stocks_nuevo = Button(ventana_principal, text= 'Nuevo', command= ingreso_stocks)
stocks_editar = Button(ventana_principal, text= 'Editar', command= editar_stocks)
stocks_ buscar = Button(ventana_principal, text= 'Buscar', command= buscar_stocks)

# Botones ventana Pedidos #

pedidos_nuevo = Button(ventana_principal, text= 'Nuevo', command= nuevo_pedido)
pedidos_editar = Button(ventana_principal, text= 'Editar', command= editar_pedido)
pedidos_buscar = Button(ventana_principal, text= 'Buscar', command= buscar_pedido)

# Botones ventana Ventas #

ventas_buscar = Button(ventana_principal, text= 'Nuevo', command= buscar_ventas)



ventana_principal.mainloop()
