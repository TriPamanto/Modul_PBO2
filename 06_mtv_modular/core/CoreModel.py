# core/CoreModeI.py
from connection import get_db
from interfaces.DosenInterface import *

class CoreModel(DosenInterfece):
  def __init__(self):
    pass

  def all(self):
    connection = get_db()
    cursor = connection.cursor()
    query = f"SELECT * FROM {self.table_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result
  
  def store(self, obj):
    connetion = get_db()
    cursor = connetion.cursor()
    set_columns = []
    set_placeholders =[]
    set_values = []

    for key, value in vars(obj).item():
      if key not in ['table_name','table_id']:
        set_columns.append(key)
        set_placeholders.append('%s')
        set_values.append(value)

    collums_string = ', '.join(set_columns)
    placeholders_string = ', '.join(set_placeholders)

    sql_query = f"INSERT INTO {self.table_name}({collums_string}) VALUES ({placeholders_string});"

    cursor.execute(sql_query, tuple(set_values))

    connetion.commit()
    cursor.close()
    connetion.close()

    def find(self, id):
      connetion = get_db()
      cursor = connetion.cursor()

      query = f"SELECT * FROM {self.table_name} WHERE {self.table_id} = %s LIMIT 1;"
      cursor.execute(query, id)
      result = cursor.fetchone()

      cursor.close()
      connetion.close()

      return result
    
    def update(self, id, dictionary):
      connetion = get_db()
      cursor = connetion.cursor()

      set_columns = []
      set_values = []

      for key, value in vars(dictionary).items():
        if key not in ['table_name','table_id']:
          column = f"{key} = %s"
          set_columns.append(column)
          set_values.append(value)

      set_column_string = ', '.join(set_columns)
      sql_query = f"UPDATE {self.table_name} SET {set_column_string} WHERE {self.table_id} = %s;"
      set_values.append(id)
      cursor.execute(sql_query, tuple(set_values))

      connetion.commit()
      cursor.close()
      connetion.close()

    def delete(sel, id):
      connetion = get_db()
      cursor = connetion.cursor()

      query = f"DELETE FROM {self.table_name} WHERE {self.table_id} = %s;"
      cursor.execute(query, (id))

      connetion.commit()
      cursor.close()
      connetion.close()