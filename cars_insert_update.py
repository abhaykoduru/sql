import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	data = (('Ford', 2013, 1000),
			('Ford', 2014, 2000),
			('Ford', 2015, 3000),
			('Honda', 2014, 10000),
			('Honda', 2015, 15000))

	c.executemany("insert into inventory values(?,?,?)", data)

	c.execute("select * from inventory")
	rows = c.fetchall()

	print "After INSERT"
	print "------------"
	for r in rows:
		print r[0], r[1], r[2]

	# update

	c.execute("update inventory set Quantity=4000\
		where Make='Ford' and Model=2014")
	c.execute("update inventory set Quantity=8000\
		where Make='Ford' and Model=2015")

	c.execute("select * from inventory")

	rows = c.fetchall()

	print "After UPDATE"
	print "------------"
	for r in rows:
		print r[0], r[1], r[2]

