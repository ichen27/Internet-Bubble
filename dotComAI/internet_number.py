import sqlite3
import pandas as pd
import plotly.express as px



conn = sqlite3.connect('stock_history.db')


query = ("""SELECT Year, "Number of Internet users" FROM "number-of-internet-users" WHERE Code = 'USA'""")
df = pd.read_sql_query(query, conn)

fig = px.line(df, 'Year', 'Number of Internet users')

fig.show()

