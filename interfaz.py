from tkinter import *
from tkinter import ttk
import base
import clase_bd as bd
### buscar info sobre treeview  https://recursospython.com/guias-y-manuales/vista-de-arbol-treeview-en-tkinter/ ###


class Ventana():
    def __init__(self) -> None:
        self.ventana_principal()

    def ventana_principal(self,):
        self.ventana_inicio = Tk()
        self.ventana_inicio.title("Negocio 2024")
        self.ventana_inicio.config(width=440, height=70)
        self.ventana_inicio.resizable(0, 0)
        self.botones()
        self.ventana_inicio.grab_set()
        self.ventana_inicio.mainloop()
        # Se crea la base de datos principal si no existe.
        self.base_datos = base.Base("Negocio_2024")
        return self.ventana_inicio

    def botones(self,):
        clientes = Button(self.ventana_inicio, text='Clientes', width=10, height=2, font=('bold', 12,),
                          command=lambda: Ventana_clientes.ventana_clientes(self,)).place(x=5, y=10)
        stocks = Button(self.ventana_inicio, text='Stocks', width=10, height=2, font=('bold', 12,),
                        command=lambda: Ventana_Stocks.ventana_stocks(self,)).place(x=115, y=10)
        pedidos = Button(self.ventana_inicio, text='Pedidos', width=10, height=2, font=('bold', 12,),
                         command=lambda: Ventana_pedidos.ventana_pedidos(self,)).place(x=225, y=10)
        ventas = Button(self.ventana_inicio, text='Ventas', width=10, height=2, font=('bold', 12,),
                        command=lambda: self.ventana_ventas(self.ventana_principal)).place(x=335, y=10)


# Ventanas secundarias #

class Ventanas_secundarias(Ventana):
    def __init__(self) -> None:
        self.ventana_secundaria()

    def ventana_secundaria(self, raiz, title, ancho=500, alto=500):
        """
        Permite crear una ventana secundaria con parametros por default.
        """

        nueva_ventana = Toplevel(raiz)
        nueva_ventana.title(title)
        nueva_ventana.config(width=ancho, height=alto)
        nueva_ventana.resizable(0, 0)
        nueva_ventana.grab_set()
        return nueva_ventana


class Ventana_clientes(Ventanas_secundarias):

    def __init__(self) -> None:
        self.ventana_clientes()

    def ventana_clientes(self,):
        """
        Crea la ventana clientes con su respectiva interfaz.
        """

        ventana = Ventanas_secundarias.ventana_secundaria(self,
                                                          self.ventana_inicio, title='Clientes', ancho=472, alto=300)
        boton_nuevo = Button(ventana, text='Nuevo', width=10, height=2, font=(
            'bold', 10,), command=lambda: Ventana_clientes.nuevo_cliente(self,))
        boton_nuevo.place(x=10, y=10)
        Button(ventana, text='Buscar', width=10, height=2, font=(
            'bold', 10,), command=None).place(x=372, y=10)
        Entry(ventana, textvariable=StringVar).place(x=230, y=30)
        Label(ventana, text='Nombre :').place(x=170, y=30)
        arbol = Tree.mostrar_treeview(
            self, ventana, 10, 60, *('Nombre', 'Telefono'))
        Tree.actualizar_tree(arbol)
        return arbol

    def nuevo_cliente(self, ):
        """
        Crea la interfaz para crear y guardar los datos de un nuevo cliente.
        """

        ventana = Ventanas_secundarias.ventana_secundaria(
            self, self.ventana_inicio, title='Nuevo cliente', ancho=200, alto=130)
        Label(ventana, text='Nombre :').place(x=10, y=10)
        Label(ventana, text='Telefono :').place(x=10, y=40)
        text_nombre = StringVar()
        text_telefono = IntVar()
        caja_nombre = Entry(ventana, textvariable=text_nombre)
        caja_nombre.place(x=70, y=10)
        caja_telefono = Entry(ventana, textvariable=text_telefono)
        caja_telefono.place(x=70, y=40)

        boton = Button(ventana, text='Guardar', width=10, height=2, font=(
            'bold', 10,), command=Ventana_clientes.guardar_nuevo_cliente)
        boton.place(x=60, y=70)
        self.datos = [caja_nombre.get(), caja_telefono.get()]

        return self.datos

    def guardar_nuevo_cliente(self,):  # Falta la sintaxis para guardar en SQL
        """
        Guarda los datos nuevos en la tabla Clientes.
        """
        base.Base.guardar_registros(self, *self.datos)
        Tree.insertar_datos_tree(self.datos)


class Ventana_Stocks(Ventana_clientes):
    def __init__(self) -> None:
        self.ventana_stocks()

    def ventana_stocks(self,):
        """
        Crea la ventana Stocks con su respectiva interfaz.
        """

        ventana = Ventanas_secundarias.ventana_secundaria(
            self, self.ventana_inicio, 'Stocks', 922, 300)
        Button(ventana, text='Nuevo producto', width=14, height=2, font=(
            'bold', 10,), command=lambda: Ventana_Stocks.nuevo_ingreso(self,)).place(x=10, y=10)
        Button(ventana, text='Buscar', width=10, height=2, font=(
            'bold', 10,), command=None).place(x=450, y=10)
        Entry(ventana, textvariable=StringVar).place(x=310, y=30)
        Label(ventana, text='Marca :').place(x=270, y=30)
        treeview = Tree.mostrar_treeview(ventana, 10, 60, *('Marca', 'Producto',
                                                            'Cantidad', 'Precio de mercado', 'Precio de venta'))
        return ventana

    def nuevo_ingreso(self,):
        """
        Crea la interfaz para crear y guardar los datos de un nuevo producto.
        """

        ventana = Ventanas_secundarias.ventana_secundaria(
            self, self.ventana_inicio, 'Nuevo producto', 250, 200)
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


class Ventana_pedidos(Ventana_Stocks):
    def __init__(self) -> None:
        self.ventana_pedidos()

    def ventana_pedidos(self,):
        """
        Crea la ventana Pedidos con su respectiva interfaz.
        """

        ventana = Ventanas_secundarias.ventana_secundaria(
            self, self.ventana_inicio, 'Pedidos', 1222, 300)
        Button(ventana, text='Nuevo', width=14, height=2, font=(
            'bold', 10,), command=lambda: Ventana_pedidos.nuevo_pedido(self,)).place(x=10, y=10)
        Button(ventana, text='Buscar', width=10, height=2, font=(
            'bold', 10,), command=None).place(x=450, y=10)
        Entry(ventana, textvariable=StringVar).place(x=310, y=30)
        Label(ventana, text='Marca :').place(x=270, y=30)
        treeview = Tree.mostrar_treeview(ventana, 10, 60, *('N° de pedido', 'Cliente', 'Marca', 'Producto',
                                                            'Cantidad', 'Precio unitario', 'Subtotal'))
        return ventana

    def nuevo_pedido(self,):
        """
        Crea la interfaz para crear y guardar los datos de un nuevo pedido.
        """

        ventana = Ventanas_secundarias.ventana_secundaria(
            self, self.ventana_inicio, title='Nuevo pedido')
        cuadro = Frame(ventana, width=430, height=350,
                       bg='blue', relief='sunken').place(x=20, y=100)
        # probar ahora si coloca el label en el frame
        Label(cuadro, text='probando').place(x=30, y=140)
        # treeview = mostrar_treeview(cuadro, 10, 60, *('N° de pedido', 'Cliente', 'Marca', 'Producto',
        #                                              'Cantidad', 'Precio unitario', 'Subtotal'))

        return ventana


class Ventana_ventas(Ventana_pedidos):
    def ventana_ventas(self, ventana_principal):
        """
        Crea la ventana Ventas con su respectiva interfaz.
        """

        pass

# Treeview #


class Tree(Ventana_ventas):
    """
    Crea un treeview.
    """

    def __init__(self,):
        """
        Metodo constructor que inicia la clase y define los atributos de instancia.
        """
        pass

    def mostrar_treeview(self, raiz, eje_x=10, eje_y=10, *columnas):
        """
        Inserta un cuadro tipo tabla para insertar los datos.
        """
        # ver si es necesario renombrar la ventana cliente, para que sea un atributo de clase #
        treeview = ttk.Treeview(
            self, self.ventana_secundaria, columns=(columnas))
        treeview.place(x=eje_x, y=eje_y)
        nueva_columna = list(columnas)
        nueva_columna.insert(0, 'ID')
        contador = 0
        for x in nueva_columna:
            treeview.column(f'#{contador}', width=150,
                            minwidth=50, stretch=True)
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

    def insertar_datos_tree(tree):
        """
        Inserta los datos dentro del treeview
        """
        # lectura de BBDD
        dato = bd.BBDD.read('clientes.db')
        print(dato)  # ver que trae y determinar la secuencia SQL a usar.
        # inserto los datos al treeview #
        Tree.insertar_datos_tree('', END, text=dato, values=[])
        return dato

    def actualizar_tree(tree):
        """ 
        Borra los datos actuales del treeview, y actualiza.
        """

        datos = tree.get_children()
        tree.delete(datos)
        datos_actualizados = Tree.insertar_datos_tree(tree)
        return datos_actualizados


### Buscar info y probar usar Listbox ###

def crear_listbox(raiz):
    """
    Crea un cuadro para listar elementos.
    """

    lista = Listbox(raiz, width=430, height=350)

    return lista
