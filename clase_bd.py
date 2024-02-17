import sqlite3 as db


class BBDD():

  def __init__(self, db_name):
    """
        Metodo constructor que inicia la clase, conecta y crea la BBDD si no existe y establece el cursor.
        """

    self.db = db_name
    self.con = db.connect(self.db)
    self.cur = self.con.cursor()

  def create_table(self,
                   table_name="Sin asignar",
                   Fk="",
                   References_table="",
                   references_field="",
                   **values):
    # Probando agegar dos parametros mas a la formula
    """
        Metodo para crear tablas, si no se especifica el nombre se crea con el nombre Sin asignar.
        """

    self.table_name = table_name

    # Se insertan los datos desde un diccionario
    sentencia_sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
    for key, value in values.items():
      sentencia_sql += f"{key} {value}, "

    sentencia_sql = sentencia_sql[:-2] + ")"
  
    # Probando claves foraneas
    clave_foranea = f" FOREIGN KEY ({Fk}) REFERENCES '{References_table}' ({references_field})"
    query = sentencia_sql + clave_foranea
    self.cur.execute(sentencia_sql)
    self.con.commit()

  def insert(self, table_name, *datos):
    """
        Metodo para insertar registros en una tabla, pasando los parametros en una tupla.
        """

    self.cur.execute(f"""INSERT INTO {table_name} VALUES((?),(?),(?))""",
                     datos)
    self.con.commit()

  def insert_more(self, table_name, *data):
    """
        Metodo para insertar varios registros al mismo tiempo en una tabla, pasando los parametros en una tupla.
        """
    # Contador de columnas para iterar y crear la sentencia sql
    contador = len(self.show_columns(table_name))

    sentencia_sql = f"INSERT INTO {table_name} VALUES ("

    for x in range(contador):
      sentencia_sql += "(?),"

    sentencia_sql = sentencia_sql[:-1] + ")"

    for x in data:
      # Creo un contador de columnas para el bucle
      n_id = len(self.read(table_name)) + 1
      # Convierto la tupla a lista
      tabla_data = list(x)
      # Agrego el id a la lista
      nuevo_id = tabla_data.insert(0, n_id)
      # Convierto la lista a tupla
      tupla_id = (tabla_data)

      self.cur.execute(sentencia_sql, tupla_id)
      self.con.commit()

  def read(self, table_name, field="*"):
    """
        Metodo para leer una tabla, por defecto selecciona todos los campos.

        Return el resultado.
        """
    self.cur.execute(f"SELECT {field} FROM {table_name}")
    self.con.commit()
    return self.cur.fetchall()

  def read_where(self, field, table_name, field_condition, logical_operator,
                 condition):
    """
        Metodo para leer una tabla, utilizando WHERE y condicion.
        Almacena el sultado con Return.
        """
    sql = f"""SELECT {field} FROM {table_name} WHERE {field_condition} {logical_operator} '{condition}'"""

    self.cur.execute(sql)
    self.con.commit()
    return self.cur.fetchall()

  def update(self, table_name, field, new_field):
    """
        Metodo para actualizar todos los registros de un campo.
        """

    self.cur.execute(f"UPDATE {table_name} SET {field} = '{new_field}'")
    self.con.commit()

  def update_where(self, table_name, field, new_data, field_condition,
                   logical_operator, condition):
    """
        Metodo para actualizar registros con WHERE, pasando como parametros el campo y la condicion.
        """

    self.cur.execute(
        f"UPDATE  {table_name} SET {field} = '{new_data}' WHERE {field_condition} {logical_operator} '{condition}'"
    )
    self.con.commit()

  def delete(self, table_name):
    """
        Metodo para eliminar todos los registros y campos de una tabla.
        """

    self.cur.execute(f"DELETE FROM {table_name}")
    self.con.commit()

  def delete_where(self, table_name, field_condition, logical_operator,
                   condition):
    """
        Metodo para eliminar los registros de una tabla, utilizando WHERE y condiciones.
        """

    self.cur.execute(
        f"DELETE FROM {table_name} WHERE {field_condition} {logical_operator} '{condition}'"
    )
    self.con.commit()

  def truncate(self, table_name):
    # investigar
    """
        Metodo para eliminar todos los registros de la tabla, dejando los campos.
        """

    self.cur.execute(f"TRUNCATE TABLE {table_name}")
    self.con.commit()

  def drop_db(self, db_name):
    # Investigar
    """
        Metodo para eliminar una base de datos.
        """

    self.cur.execute(f"DROP DATABASE '{db_name}'")
    self.con.commit()

  def drop_table(self, table_name):
    """
        Metodo para eliminar una tabla.
        """

    self.cur.execute(f"DROP TABLE '{table_name}'")
    self.con.commit()

  def show_table(self, ):
    """
        Metodo para mostrar las tablas de la base de datos.
        """

    self.cur.execute("SELECT name from sqlite_master where type= 'table'")
    self.con.commit()
    return self.cur.fetchall()

  def show_columns(self, table_name):
    """
        Metodo para lista todos los campos de una tabla.
        """

    self.cur.execute(f"SELECT name FROM pragma_table_info('{table_name}')")
    self.con.commit()
    return self.cur.fetchall()

  def query_operation(self, operation, field, table_name):
    """
        Metodo que devuelve una tabla provisoria.
        """

    self.cur.execute(f"SELECT {operation} ({field}) FROM {table_name} ")
    self.con.commit()
    return self.cur.fetchall()

  def query(self):
    """
        Metodo que devuelve una tabla provisoria.
        """
  
    self.cur.execute(f"""SELECT Cliente, N° Pedido, Marca, Producto, Cantidad, Precio_unitario   FROM  clientes, ventas, pedidos, stocks""")
    self.con.commit()
    return self.cur.fetchall()
  

###################################################################################
