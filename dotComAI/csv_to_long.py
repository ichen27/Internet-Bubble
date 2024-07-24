import csv
import sqlite3
import os
import pandas as pd


dir = '/home/ivan-chen/Downloads/Computer_Science/dotComAI/data/dotComhist'

df_list = []

for filename in os.listdir(dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(dir, filename)
        df = pd.read_csv(file_path)
        df['Company'] = filename.replace('.csv', '')
        df_list.append(df)

long_format_df = pd.concat(df_list, ignore_index=True)

conn = sqlite3.connect('stock_history.db')

long_format_df.to_sql('dot_com_prices', conn, if_exists='replace', index=False)

conn.commit()
conn.close()