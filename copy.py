import sqlite3

src = sqlite3.connect("source.db")
dst = sqlite3.connect("target.db")

s = src.cursor()
d = dst.cursor()

d.execute("CREATE TABLE users (id INTEGER, name TEXT)")

s.execute("SELECT * FROM users")
rows = s.fetchall()

for r in rows:
    d.execute("INSERT INTO users VALUES (?,?)", r)

dst.commit()
src.close()
dst.close()

print("Data copied")
