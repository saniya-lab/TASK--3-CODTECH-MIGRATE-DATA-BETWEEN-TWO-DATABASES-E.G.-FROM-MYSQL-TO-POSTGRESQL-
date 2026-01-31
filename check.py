import sqlite3

src = sqlite3.connect("source.db")
dst = sqlite3.connect("target.db")

s = src.cursor()
d = dst.cursor()

s.execute("SELECT COUNT(*) FROM users")
d.execute("SELECT COUNT(*) FROM users")

print("Source rows:", s.fetchone()[0])
print("Target rows:", d.fetchone()[0])

src.close()
dst.close()
