import sqlite3
conn = sqlite3.connect('hubei_2016_full.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

try:
    print("Bridge count (L24a):", conn.execute("SELECT COUNT(*) FROM L24a WHERE col0 LIKE '%107%'").fetchone())
    print("Bridge count (L24a大桥):", conn.execute("SELECT COUNT(*) FROM L24a WHERE col0 LIKE '%107%' AND (col13 LIKE '%大桥%' OR col13 LIKE '%中桥%')").fetchone())
except Exception as e:
    print(e)
