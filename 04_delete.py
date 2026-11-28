# D. DELETE – Remove Employee

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="company_db"
)

cursor = conn.cursor()

query = "DELETE FROM employees WHERE emp_id = %s"

cursor.execute(query, (4,))

conn.commit()

print("Employee deleted successfully!")

cursor.close()
conn.close()