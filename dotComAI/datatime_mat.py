import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import sqlite3
import matplotlib.dates as mdates

conn = sqlite3.connect('stock_history.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()


for table in tables:
    if table[0][-3:] == "dot":
        query = f"SELECT Date, Open FROM {table[0]} WHERE Open IS NOT NULL"
        df = pd.read_sql_query(query, conn)
        df['Date'] = pd.to_datetime(df['Date'])
        plt.plot(df['Date'], df['Open'], label=table[0])


plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=90)
plt.legend(loc='upper left')

plt.xlabel("Date")
plt.ylabel("Stock Price")

plt.show()


conn.commit()
conn.close()