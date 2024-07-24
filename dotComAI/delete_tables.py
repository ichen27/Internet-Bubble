import sqlite3


conn = sqlite3.connect('stock_history.db')
c = conn.cursor()

table_list = ["005930.KS_ai"]

for table in table_list:
    c.execute(f'DROP TABLE IF EXISTS "{table}"')

conn.commit()
conn.close()

