# *Hands-on Assignment (30 Marks)*

# Create a Python program for a Student Management System that:


# Student Management System :

# Global variable : Take College as global variable.

college_name = "Bharati Vidhyaeeth's College of Engineering"


# Student details : Takes student name, age, roll number.

student_name = "Atharva Satpute"

age = 21

roll_num = 22


# Stores marks for 5 subjects (Multiple Assignment).

python_marks, sql_marks, excel_marks, powerbi_marks, ai_marks = 85, 80, 90, 67, 95

# Calculate:

# Total Marks

total_marks = python_marks + sql_marks + excel_marks + powerbi_marks + ai_marks

# Average Marks

average_marks = total_marks / 5

# Percentage

percentage = (total_marks / 500) * 100


# Swapping two variables

# Before Swapping

print("Before Swapping")

print(f"Python Marks : {python_marks}")

print(f"SQL Marks : {sql_marks}")

# Swapping Variables

python_marks, sql_marks = sql_marks, python_marks

#After Swapping

print("\nAfter Swapping")

print(f"Python Marks : {python_marks}")

print(f"SQL Marks : {sql_marks}")


# Display student information

print("\n=================================")
print(" STUDENT MANAGEMENT SYSTEM ")
print("=================================")


# Displays the output using f-strings.

print(f"College name : {college_name}")

print(f"My name is  {student_name}")

print(f"I am {age} years old")

print(f"My Roll Number : {roll_num}")


print("\n------ Subject Marks ------")

print(f"Python Marks : {python_marks}")

print(f"SQL Marks : {sql_marks}")

print(f"Excel Marks : {excel_marks}")

print(f"Power Bi Marks : {powerbi_marks}")

print(f"AI Marks : {ai_marks}")


print("\n------ Result ------")

print(f"Total Marks : {total_marks}")

print(f"Average Marks : {average_marks}")

print(f"Percentage : {percentage}%")


print("\nCongratulations!")

print(f"{student_name} has successfully completed the examination.")