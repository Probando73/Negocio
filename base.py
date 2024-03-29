import clase_bd as bd


class Base(bd.BBDD):
    """
    Permite la interaccion con la clase BBDD, y poder gestionar mediante la app.
    """

    def __init__(self,):
        """
        Metodo constructor que inicia la clase y define las variables de instancia.
        """

        # Se crea la base de datos principal si no existe.
        self.base_datos = bd.BBDD("Negocio_2024")

        # Diccionarios con los nombres de las tablas y tipo de campo.
        self.tabla_clientes = {
            'ID': 'INTEGER  AUTO_INCREMENT PRIMARY KEY',
            'Cliente': 'TEXT NOT NULL',
            'Telefono': 'INTEGER NOT NULL',
        }

        self.tabla_ventas = {
            'N° Pedido': 'INTEGER AUTO_INCREMENT PRIMARY KEY',
            'Cliente': 'TEXT NOT NULL ',
            'Cant_Productos': 'INTEGER NOT NULL',
            'Monto': 'INTEGER NOT NULL',
        }

        self.tabla_pedidos = {
            'ID': 'INTEGER AUTO_INCREMENT ',
            'N° Pedido': 'INTEGER PRIMARY KEY',
            'Cliente': 'TEXT NOT NULL',
            'Marca': 'TEXT NOT NULL',
            'Producto': 'TEXT NOT NULL',
            'Cantidad': 'INTEGER NOT NULL',
            'Precio_unitario': 'INTEGER NOT NULL',
            'Subtotal': 'INTEGER NOT NULL',
        }

        self.tabla_stocks = {
            'ID': 'INTEGER  AUTO_INCREMENT',
            'Marca': 'TEXT NOT NULL',
            'Producto': 'TEXT  NOT NULL PRIMARY KEY',
            'Cantidad': 'INTEGER NOT NULL',
            'Precio_mercado': 'INTEGER NOT NULL',
            'Precio_de_venta': 'INTEGER NOT NULL',
        }

        self.creacion_tablas()

    def creacion_tablas(self,):
        """
        Metodo para crear las tablas de la base
        """

        # Se crean las tablas en la BBDD

        self.clientes = bd.BBDD.create_table("clientes", **self.tabla_clientes)
        self.ventas = bd.BBDD.create_table("ventas",
                                           Fk='Cliente',
                                           References_table='clientes',
                                           references_field='ID',
                                           **self.tabla_ventas)

        self.tabla_pedidos = bd.BBDD.create_table("pedidos",
                                                  Fk='N° Pedido',
                                                  References_table='ventas',
                                                  references_field='N° Pedido',
                                                  **self.tabla_pedidos)

        self.tabla_stocks = bd.BBDD.create_table("stocks",
                                                 Fk='Precio_de_venta',
                                                 References_table='pedidos',
                                                 references_field='Precio_unitario',
                                                 **self.tabla_stocks)

    def lectura_tabla(self, table):
        """
        Metodo para leer los datos de una tabla
        """

        lectura = bd.BBDD.read(self, table)

    def guardar_nuevo_cliente(self, *datos):
        """
        Metodo para insertar datos en una tabla.
        """
        bd.BBDD.insert_more(self, self.clientes, *datos)
