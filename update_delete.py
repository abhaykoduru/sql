# update and delete statements

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# update data
	c.execute("update population set population = 9000000 where city = 'New York City'")

	# delete data
	c.execute("delete from population where city = 'Boston'")

	print "\nNEW DATA:\n"

	c.execute("select * from population")
	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]
