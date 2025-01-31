import sqlite3

# connecting to the database
connection = sqlite3.connect("test.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
table = """CREATE TABLE books (
ISBN CHAR(17),
Name VARCHAR(30),
Author VARCHAR(30),
Quote VARCHAR(300)
)"""

# execute the statement
crsr.execute(table)

table = """CREATE TABLE read (
ISBN CHAR(17),
start DATE,
end DATE, 
PRIMARY KEY (ISBN, start)
)"""
crsr.execute(table)

table = """CREATE TABLE author (
ID INTEGER,
Name VARCHAR(30),
Surname VARCHAR(30)
)"""
crsr.execute(table)

crsr.execute('''INSERT INTO books VALUES ('978-1-250-09526-8', 'Caraval', 1, NULL)''')
crsr.execute('''INSERT INTO books VALUES ('978-1-250-09532-9', 'Legendary', 1,
'Only those who persevere can find their true ending.')''')
crsr.execute('''INSERT INTO books VALUES ('978-1-250-15768-3', 'Finale', 1,
'I think the most magnificent things are worth living for.')''')
crsr.execute('''INSERT INTO books VALUES ('978-1-250-36890-4', 'Spectacular', 1, NULL)''')

crsr.execute('''INSERT INTO books VALUES ('978-1-529-38094-1', 'Once Upon A Broken Heart', 1,
'Every story has the potential for infinite endings.')''')
crsr.execute('''INSERT INTO books VALUES ('978-1-529-38100-9', 'The Ballad Of Never After', 1,
'There is nothing of equal value to me.')''')
crsr.execute('''INSERT INTO books VALUES ('978-1-529-39932-5', 'A Curse For True Love', 1,
'She had forgotten how hope could make colors brighter and feelings warmer, how it could shift thoughts from what wasnt to what was possible.')''')

crsr.execute('''INSERT INTO read VALUES ('978-1-250-09526-8', '2024-08-29', '2024-09-17')''')
crsr.execute('''INSERT INTO read VALUES ('978-1-250-09532-9', '2024-09-17', '2024-12-26')''')
crsr.execute('''INSERT INTO read VALUES ('978-1-250-15768-3', '2024-12-26', '2024-12-29')''')

crsr.execute('''INSERT INTO read VALUES ('978-1-529-38094-1', '2024-12-29', '2024-12-30')''')
crsr.execute('''INSERT INTO read VALUES ('978-1-529-38100-9', '2024-12-30', '2025-01-03')''')
crsr.execute('''INSERT INTO read VALUES ('978-1-529-39932-5', '2025-01-04', '2025-01-23')''')

crsr.execute('''INSERT INTO read VALUES ('978-1-250-36890-4', '2025-01-23', '2025-01-24')''')

crsr.execute('''INSERT INTO author VALUES (1, 'Stephanie', 'Garber')''')
connection.commit()

# close the connection
connection.close()