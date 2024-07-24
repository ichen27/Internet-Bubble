import pandas as pd
import csv
import sqlite3
import os # library to access directories


conn = sqlite3.connect('stock_history.db')
c = conn.cursor()

dir = '/home/ivan-chen/Downloads/Computer_Science/dotComAI/data'

def csv_to_sqlite(csv_file, file_name, cursor, connection):
    df = pd.read_csv(csv_file)
    file_name = file_name.replace('.csv', '')
    #file_name = file_name + '_ai'
    df.to_sql(name=file_name, con=connection, if_exists='replace')
    print(f"File: {file_name} has been successfully saved")



for filename in os.listdir(dir):
    file_path = os.path.join(dir, filename) #gets file path
    if os.path.isfile(file_path): #Checks if file exists
        csv_to_sqlite(file_path, filename, c, conn)


conn.commit()
conn.close()