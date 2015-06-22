# Create a SQLite3 database and table

# impirt the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table 
#cursor.execute("""CREATE TABLE population
#				(city TEXT, state TEXT, population INT)
#					""")

# inserting some data
cursor.execute("insert into population VALUES('Boulder', 'Colorado', 103166)")

cursor.execute("insert into population VALUES('Huntsville', 'Alabama', 186254)")

# commit the changes
conn.commit()

# close the database connectionation 
conn.close()