# Database connection

# Suppose you're connection Python to MySQL.

try:
    import mysql.connector

    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        database = "college"
    )

    print("Database connected successfully")

except mysql.connector.Error as e:
    print("Database connection failed:", e)