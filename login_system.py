correct_password = "admin123"

try:
    password = input("Enter password: ")

    if password != correct_password:
        raise Exception("Incorrect password")

    print("Login successful")

except Exception as e:
    print("Login failed:", e)