import pyodbc as pyodbc

import pyodbc_SQL

# Establish a connection to the SQL Server
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=your_server_name;"
    "Database=your_database_name;"
    "UID=your_username;"
    "PWD=your_password;"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute an SQL query
cursor.execute("SELECT * FROM your_table_name")

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
