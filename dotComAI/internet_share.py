import sqlite3
import pandas as pd
import plotly.express as px



conn = sqlite3.connect('stock_history.db')


query = ("""SELECT Year, "Individuals using the Internet (% of population)" FROM "share-of-individuals-using-the-internet" WHERE Code = 'USA'""")
df = pd.read_sql_query(query, conn)

fig = px.line(df, 'Year', 'Individuals using the Internet (% of population)')

fig.show()

