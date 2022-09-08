import sqlite3 as sq
import pandas as pd

def pull_csv():
    # Create a connection object
    connection = sq.connect('sih.db')

    # Create a cursor object
    curs = connection.cursor()

    # Load CSV data into Pandas DataFrame
    output = pd.read_csv('output.csv')

    # Write the data to a sqlite db table
    output.to_sql('output', connection, if_exists='replace', index=False)

    # Close connection to SQLite database
    connection.close()