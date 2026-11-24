import mysql.connector

# Establish database connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@130305_",
    database="company_dbase"
)

if conn.is_connected():
    print("Connected to MySQL Successfully!")

# Close connection

conn.close()