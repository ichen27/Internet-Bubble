import numpy as np
import pandas as pd
import datetime
import sqlite3
import matplotlib.dates as mdates
import plotly.express as px
import plotly.graph_objects as go

conn = sqlite3.connect('stock_history.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()

fig = go.Figure()
for table in tables:
    if table[0][-3:] == "dot":
        query = f"SELECT Date, Open FROM {table[0]} WHERE Open IS NOT NULL"
        df = pd.read_sql_query(query, conn)
        df['Date'] = pd.to_datetime(df['Date'])
        print(f"Data from table {table[0]}:", df.head())
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Open'], mode='lines', name=table[0]))

fig.update_layout(title='Dot Com Bubble Stock Prices', xaxis_title='Date', yaxis_title='stock price')
fig.show()

conn.commit()
conn.close()