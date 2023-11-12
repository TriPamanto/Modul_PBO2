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
  
  def store(dosen_obj):
    connetion = get_db()
    cursor = connetion.cursor()
    set_collumns = []
    set_placeholders =[]
    set_values = []

    for key, value in vars(obj).item():
      if key not in ['table_name','table_id']:
        set_collumns.append(key)
        set_placeholders.append('%s')
        set_values.append(value)

    collums_string = ', '.join(set_collumns)
    placeholders_string = ', '.join(set_placeholders)

    sql_query = f"INSERT INTO {self.table_name}({collums_string})
    VALUES ({placeholders_string});"

    cursor.execute(sql_query, tuple(set_values))

    connetion.commit()
    cursor.close()
    connetion.close()

    def find(self, id)
      connetion = get_db()

    