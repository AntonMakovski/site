import sqlite3 as sql

base = sql.connect('data_base.db')
cursor = base.cursor()
cursor.execute("""CREATE TABLE coments (coments VARCHAR)""")
