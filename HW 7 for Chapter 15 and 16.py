import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Load data from the existing CSV file
data = pd.read_csv('classic_rock_playlist.csv')

# Create a new table and insert data from the CSV file
data.to_sql('rock_table', conn, index=False)

# Retrieve data from the table
data = pd.read_sql_query("SELECT * FROM rock_table", conn)

# Export the data to a CSV file
data.to_csv('rock_table_new.csv', index=False)

# Close the connection to the database
conn.close()
