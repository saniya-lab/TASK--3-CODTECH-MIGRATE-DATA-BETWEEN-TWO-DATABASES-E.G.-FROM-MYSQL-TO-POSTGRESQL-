import sqlite3

db = sqlite3.connect("source.db")
cur = db.cursor()

cur.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cur.execute("INSERT INTO users VALUES (1,'Ram')")
cur.execute("INSERT INTO users VALUES (2,'Sita')")

db.commit()
db.close()

print("Source database created")
