import csv

# # Import pyodbc to connect to SQL Server database
import pyodbc 

# Building connection string to the database

conn_str = (
    r'driver={ODBC Driver 18 for SQL Server};'
    r'server=(local);'
    r'database=GrocerySales;'
    r'trusted_connection=yes;'
    r'TrustServerCertificate=yes;'
    )

# Connection to the database

cnxn = pyodbc.connect(conn_str)

# Use to execute sql queries

cursor = cnxn.cursor()

cursor.execute('SELECT * FROM Sales')

for row in cursor:
    print(row)


# Committing the changes to the database

cnxn.commit()

# Closing the database connection

cnxn.close()
print("From database!")