import sqlite3

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()

	# insert multiple records using a tuple
	cities = [('Boston', 'MA', 600000),
				('Chicago', 'IL', 2700000),
				('Houston', 'TX', 2100000),
				('Phoenix', 'AZ', 1500000)]
	c.executemany('insert into population VALUES(?,?,?)', cities)