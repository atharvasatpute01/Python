# Perform CRUD Operations
# CRUD means Create, Read, Update and Delete.

# A. INSERT – Add Employee

import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL@130305_",
    database = "company_dbase"
)

cursor = conn.cursor()

query = """
INSERT INTO employees
(emp_name, department, salary, city)
VALUES (%s, %s, %s, %s)
"""

values = (
    "Sneha",
    "Python Development",
    48000,
    "Pune"
)

cursor.execute(query, values)

conn.commit()

print("Employee inserted successfully!")

cursor.close()
conn.close()