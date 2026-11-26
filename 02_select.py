# B. SELECT – Retrieve Employees

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="company_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")

records = cursor.fetchall()

for row in records:
    print(row)

cursor.close()
conn.close()