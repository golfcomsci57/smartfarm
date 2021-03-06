import sqlite3

conn = sqlite3.connect('include/smartfarm.db')

conn.execute('''CREATE TABLE CM
         (ID			INTEGER PRIMARY KEY AUTOINCREMENT,
         CM			TEXT 				NOT NULL,
         DATETIME		DATETIME   			NOT NULL);''')

conn.execute('''CREATE TABLE LITRE
         (ID			INTEGER PRIMARY KEY AUTOINCREMENT,
         LITRE			TEXT 				NOT NULL,
         DATETIME		DATETIME   			NOT NULL);''')

conn.execute('''CREATE TABLE FEED
         (ID			INTEGER PRIMARY KEY AUTOINCREMENT,
         DATETIME		DATETIME   			NOT NULL);''')
conn.close()
