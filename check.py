import sqlite3
import json

db = sqlite3.connect('hubei_2025.db')
cursor = db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [r[0] for r in cursor.fetchall()]

results = {}
for table in tables:
    cursor.execute(f"SELECT * FROM {table} LIMIT 1;")
    cols = [desc[0] for desc in cursor.description]
    results[table] = cols

print(json.dumps(results, ensure_ascii=False, indent=2))
