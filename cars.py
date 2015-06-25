import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("create table inventory (Make TEXT, Model INT, Quantity INT)")

conn.close()