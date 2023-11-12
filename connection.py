import pymysql

def get_db():
  connection = pymysql.connect(
    host='localhost',
    use='root',
    password='root',
    database='pbo2',
    cursorclass=pymysql.cursors.DictCursor
  )
  return connection