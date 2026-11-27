# C. UPDATE – Modify Employee Salary

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="company_db"
)

cursor = conn.cursor()

query = """
UPDATE employees
SET salary = %s
WHERE emp_id = %s
"""

values = (70000, 1)

cursor.execute(query, values)

conn.commit()

print("Employee salary updated!")

cursor.close()
conn.close()