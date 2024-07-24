import sqlite3


conn = sqlite3.connect('stock_history.db')
c = conn.cursor()

key = "ai"

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()

for table in tables:
    if table[0][-2:] == 'ot':
        c.execute(f'DROP TABLE IF EXISTS {table[0]}')
        print(f'Dropped {table[0]}')