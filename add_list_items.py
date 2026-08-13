# *Add List Items*

# There are three important methods:

# append()
# insert()
# extend()




# 1. append() – Add at the End

# append() adds one item at the end of the list.

students = ["Amit", "Rahul", "Priya"]

students.append("Neha")

print(students)

# Important: append() always adds the item at the end.




# 2. insert() – Add at a Specific Position

# insert() allows us to specify where the new item should be added.

# Syntax :

# list.insert(index, value)

# Example :

students = ["Amit", "Rahul", "Priya"]

students.insert(1, "Naha")

print(students)




# 3. Insert at the Beginning

# Use index 0.

cars = ["Audi", "Mercedes", "Toyota"]

cars.insert(0, "Volvo")

print(cars)




# 4. Insert Before the Last Item

# You can also use negative indexing.

languages = ["Python", "Java", "C++", "PHP"]

languages.insert(-1, "JavaScript")

print(languages)




# 5. extend() – Add Multiple Items

# extend() is used to add multiple items to the end of a list.

students = ["Amit", "Rahul"]

students.extend(["Priya", "Neha", "Karan"])

print(students)




# 6. append() vs extend()

# This is a very important interview concept.

# Using append()

fruits = ["Apple", "Banana"]

fruits.append(["Mango", "Orange"])

print(fruits)

# Using extend()

fruits = ["Apple", "Banana"]

fruits.extend(["Mango", "Orange"])

print(fruits)

# Remember

# append()  → adds one object
# extend()  → adds items from another iterable




# 7. Adding Numbers

numbers = [10, 20, 30]

numbers.append(40)

numbers.extend([50, 60, 70])

print(numbers)




# 8. Real-World Example – Shopping Cart

cart = ["Laptop", "Mouse"]

print("Shopping Cart :", cart)

# Adding multiple products :

cart.extend(["Monitor", "Webcam", "Headphones"])

print("Shopping Cart :", cart)




# 9. User Input with append()

students = []

name1 = input("Enter student name : ")
students.append(name1)

name2 = input("Enter student name : ")
students.append(name2)

print("Students :", students)




# 10. Add Items Using a Loop

# This is very useful in real programs.

students = []

for i in range(5):
    name = input("Enter student name : ")
    students.append(name)

print("Students :", students)