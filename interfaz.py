from tkinter import *
from tkinter import ttk

### buscar info sobre treeview  https://recursospython.com/guias-y-manuales/vista-de-arbol-treeview-en-tkinter/ ###

### Funciones ###

# Ventanas secundarias #


def ventana_secundaria(raiz, title, ancho=500, alto=500):
    """
    Permite crear una ventana secundaria con parametros por default.
    """

    nueva_ventana = Toplevel(raiz)
    nueva_ventana.title(title)
    nueva_ventana.config(width=ancho, height=alto)
    nueva_ventana.resizable(0, 0)
    nueva_ventana.grab_set()
    return nueva_ventana


def ventana_clientes():
    """
    Crea la ventana clientes con su respectiva interfaz.
    """

    ventana = ventana_secundaria(
        ventana_principal, 'Clientes', ancho=472, alto=300)
    Button(ventana, text='Nuevo', width=10, height=2, font=(
        'bold', 10,), command=nuevo_cliente).place(x=10, y=10)
    Button(ventana, text='Buscar', width=10, height=2, font=(
        'bold', 10,), command=None).place(x=372, y=10)
    Entry(ventana, textvariable=StringVar).place(x=230, y=30)
    Label(ventana, text='Nombre :').place(x=170, y=30)
    mostrar_treeview(ventana, 10, 60, *('Nombre', 'Telefono'))
    return ventana


def guardar_cliente(nombre, telefono):  # Falta la sintaxis para guardar en SQL
    """
    Guarda los datos nuevos en la tabla Clientes.
    """

    print(nombre)
    print(telefono)
    return guardar_cliente


def nuevo_cliente():
    """
    Crea la interfaz para crear y guardar los datos de un nuevo cliente.
    """

    ventana = ventana_secundaria(
        ventana_principal, 'Nuevo cliente', ancho=200, alto=130)
    Label(ventana, text='Nombre :').place(x=10, y=10)
    Label(ventana, text='Telefono :').place(x=10, y=40)
    text_nombre = StringVar()
    text_telefono = IntVar()
    caja_nombre = Entry(ventana, textvariable=text_nombre)
    caja_nombre.place(x=70, y=10)
    caja_telefono = Entry(ventana, textvariable=text_telefono)
    caja_telefono.place(x=70, y=40)
    nuevo_nombre = str(caja_nombre.get())
    nuevo_telefono = int(caja_telefono.get())
    print(nuevo_nombre)
    print(nuevo_telefono)
    Button(ventana, text='Guardar', width=10, height=2, font=(
        'bold', 10,), command=lambda: guardar_cliente(nuevo_nombre, nuevo_telefono)).place(x=60, y=70)

    return ventana, nuevo_nombre, nuevo_telefono


def ventana_stocks():
    """
    Crea la ventana Stocks con su respectiva interfaz.
    """

    ventana = ventana_secundaria(ventana_principal, 'Stocks', 922, 300)
    Button(ventana, text='Nuevo producto', width=14, height=2, font=(
        'bold', 10,), command=nuevo_ingreso).place(x=10, y=10)
    Button(ventana, text='Buscar', width=10, height=2, font=(
        'bold', 10,), command=None).place(x=450, y=10)
    Entry(ventana, textvariable=StringVar).place(x=310, y=30)
    Label(ventana, text='Marca :').place(x=270, y=30)
    treeview = mostrar_treeview(ventana, 10, 60, *('Marca', 'Producto',
                                                   'Cantidad', 'Precio de mercado', 'Precio de venta'))
    return ventana


def nuevo_ingreso():
    """
    Crea la interfaz para crear y guardar los datos de un nuevo producto.
    """

    ventana = ventana_secundaria(ventana_principal, 'Nuevo producto', 250, 200)
    labels = ('Marca', 'Producto', 'Cantidad',
              'Precio de mercado', 'Precio de venta')
    y = 10
    y_e = 10
    for x in labels:
        Label(ventana, text=f'{x} :', justify=CENTER).place(x=10, y=y)
        # ver de crear un diccionario con el tipo de dato
        Entry(ventana, textvariable=StringVar).place(x=120, y=y_e)
        y += 30
        y_e += 30

    Button(ventana, text='Guardar', width=10, height=1, font=(
        'bold', 10,), command=None).place(x=90, y=160)
    return ventana


def ventana_pedidos():
    """
    Crea la ventana Pedidos con su respectiva interfaz.
    """

    ventana = ventana_secundaria(ventana_principal, 'Pedidos', 1222, 300)
    Button(ventana, text='Nuevo', width=14, height=2, font=(
        'bold', 10,), command=nuevo_pedido).place(x=10, y=10)
    Button(ventana, text='Buscar', width=10, height=2, font=(
        'bold', 10,), command=None).place(x=450, y=10)
    Entry(ventana, textvariable=StringVar).place(x=310, y=30)
    Label(ventana, text='Marca :').place(x=270, y=30)
    treeview = mostrar_treeview(ventana, 10, 60, *('N° de pedido', 'Cliente', 'Marca', 'Producto',
                                                   'Cantidad', 'Precio unitario', 'Subtotal'))
    return ventana


def nuevo_pedido():
    """
    Crea la interfaz para crear y guardar los datos de un nuevo pedido.
    """

    ventana = ventana_secundaria(ventana_principal, 'Nuevo pedido')
    cuadro = Frame(ventana, width=430, height=350,
                   bg='blue', relief='sunken').place(x=20, y=100)
    # probar ahora si coloca el label en el frame
    Label(cuadro, text='probando').place(x=30, y=140)
    # treeview = mostrar_treeview(cuadro, 10, 60, *('N° de pedido', 'Cliente', 'Marca', 'Producto',
    #                                              'Cantidad', 'Precio unitario', 'Subtotal'))

    return ventana


def ventana_ventas():
    """
    Crea la ventana Ventas con su respectiva interfaz.
    """

    return ventana_secundaria(ventana_principal, 'Ventas')


### Buscar info y probar usar Listbox ###

def crear_listbox(raiz):
    """
    Crea un cuadro para listar elementos.
    """

    lista = Listbox(raiz, width=430, height=350)

    return lista
# Treeview #


def mostrar_treeview(raiz, eje_x=10, eje_y=10, *columnas):
    """
    Inserta un cuadro tipo tabla para insertar los datos.
    """

    treeview = ttk.Treeview(raiz, columns=(columnas))
    treeview.place(x=eje_x, y=eje_y)
    nueva_columna = list(columnas)
    nueva_columna.insert(0, 'ID')
    contador = 0
    for x in nueva_columna:
        treeview.column(f'#{contador}', width=150, minwidth=50, stretch=True)
        treeview.heading(f'#{contador}', text=x)
        contador += 1
    return treeview


def mostrar_seleccion():
    """
    Muestra la informacion seleccionada
    """

    foco = ttk.Treeview.focus()  # probar si guarda el dato del puntero
    valor = ttk.Treeview.selection()  # ver que muestra en la seleccion.
    # lista_multiple= Listbox(raiz, selectmode = "multiple") # probar la seleccion multiple
    print('Foco puesto en: ', foco)
    print('valor de seleccion: ', valor)

################## Se crea ventana principal, titulo y tamaño ##################


ventana_principal = Tk()
ventana_principal.title("Negocio 2024")
ventana_principal.config(width=440, height=70)
ventana_principal.resizable(0, 0)

################## Ventanas secundarias ##################


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
