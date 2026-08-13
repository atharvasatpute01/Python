# A list stores multiple values inside a single variable.

students = ["Amit", "Rahul", "Priya", "Neha"]

print(students)




# A list uses square brackets [] and items are separated using commas.

# Lists can contain different data types

names = ["Amiit", "Rahul", "Priya"]

marks = [78, 85, 92, 67]

prices = [99.50, 150.75, 500.00]

data = ["Amit", 21, 85.5, True]

print(names)

print(marks)

print(prices)

print(data)




# len() — number of items.

cars = ["Mercedes", "Audi", "Volvo", "Toyota"]

print(len(cars))




# List indexing

# Python starts counting from 0.

# Index :          0       1        2         3
#         ["Mercedes", "Audi", "Volvo", "Toyota"]

cars = ["Mercedes", "Audi", "Volvo", "Toyto"]

print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])




# Write a Python program that creates :

# students = ["Amit", "Priya", "Rahul", "Sneha", "Karan"]

# Display the complete list, numbers of the students, data type of the variable, first student, third student, and last student.


students = ["Amit", "Priya", "Rahul", "Sneha", "Karan"]

# Display complete list
print("\nStudent List:", students)

# Display number of students
print("\nNumber of Students:", len(students))

# Display data type
print("\nData Type:", type(students))

# Display first student
print("\nFirst Student:", students[0])

# Display third student
print("\nThird Student:", students[2])

# Display last student
print("\nLast Student:", students[-1])




# Access List Items

# 1. Access Items Using Index

# Python list indexing starts from 0.

fruits = ["Apple", "Banana", "Mango", "Orange", "Graphs"]

print(fruits[0])
print(fruits[1])
print(fruits[2])


# 2. Negative Indexing

# Negative indexing accesses elements from the end of the list.

#   -5        -4       -3        -2        -1
# Apple    Banana    Mango    Orange    Grapes

# Example :

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])


# 3. List Slicing

# Slicing allows us to access multiple items.

# Syntax :

# list[start:end]

# Example :

cars = ["Mercedes", "Audi", "Volvo", "Toyota", "Honda", "Kia"]

print(cars[1:4])

# 1:4 means :

# Start from index 1
# Stop BEFORE index 4

# returns indexes : 1, 2, 3


# 4. Slice From Beginning

# If the starting index is missing, Python starts from index 0.

cars = ["Mercedes", "Audi", "Volvo", "Toyota", "Honda", "Kia"]

print(cars[:3])


# 5. Slice Until the End

# If the ending index is missing, Python continues until the end.

cars = ["Mercedes", "Audi", "Volvo", "Toyota", "Honda", "Kia"]

print(cars[2:])


# 6. Negative Index Slicing

# Negative indexes can also be used with slicing.

cars = ["Mercedes", "Audi", "Volvo", "Toyota", "Honda", "Kia"]

print(cars[-4:-1])

# Again, the last index is not included.


# 7. Check if an Item Exists

# Use the in operator.

cars = ["Mercedes", "Audi", "Volvo", "Toyota"]

if "Volvo" in cars:
    print("Volvo is available")

# You also can use not in :

if "Honda" not in cars:
    print("Honda is not available")


# 8. Slicing with step

# The complete slicing syntac is :

# list[start:end:step]

# Example :

numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[0:7:2])

# Here 2 means take every second element.

# Another shortcut :

print(numbers[::2])