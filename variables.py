# Practice

# Create variables

# student_name
# college_name
# city
# mobile_number
# age
# cgpa

# Print all variables.

student_name = "Atharva"
college_name = "Bharati Vidhyapeeth's College of Engineering"
city = "Kolhapur"
mobile_number = 8282821010
age = 21
cgpa = 7

print(student_name)
print(college_name)
print(city)
print(mobile_number)
print(age)
print(cgpa)




# Example 1 :

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# Example 2 :

# Assign same value

x = y = z = 100

print(x)
print(y)
print(z)

# Example 3 :

name, age, city = "Atharva", 21, "Kolhapur"

print(name)
print(age)
print(city)




# Practice

# Create : product, price, quantity

# Assign in one line.

product, price, quantity = "Laptop", 70000, 5

print(product)
print(price)
print(quantity)




# Print variables using different methods.

# Method 1 :

name = "Atharva"

print(name)

# Method 2 :

name = "Atharva"
age = 21

print(name, age)

# Method 3 :

# Using +

first = "Hello"
second = "World"

print(first + "" + second)

# Method 4 :

# Using f-string (Most Used)

namme = "Atharva"
age = 22

print(f"My name is {name}.")
print(f"I am {age} years old.")

# Practice

# Store : Company, Designation, Salary

company = "Syntova"
designation = "Data Engineer"
salary = 50000

print(f"I am working at {company}.")
print(f"I am a {designation}.")
print(f"I have a salary of {salary}.")




# Global Variables :

# A variable created outside a function is called a global variable.

company = "Google"

def employee():
    print(company)

employee()


# Example 

country = "India"

def show():
    print(country)

show()

print(country)


# Global Keyword

count = 10

def update():
    global count
    count = 20

update()

print(count)




# Variable Exercises :

# Exercise 1

# Store your personal details

# Name
# Age
# College
# CGPA

# Print everything.

name = "Atharva"
age = 21
college = "Bharati Vidhyapeeth's College of Engineering"
cgpa = 7.5

print(name)
print(age)
print(college)
print(cgpa)


# Exercise 2

# Store

# Laptop Brand
# RAM
# Storage
# Price

# Print using f-string.

Laptop_Brand = "Apple"
RAM = "32 GB"
Storage = "1 TB"
Price = 2500

print(f"Laptop Brand : {Laptop_Brand}")
print(f"RAM          : {RAM}")
print(f"Storage      : {Storage}")
print(f"Price        : ${Price}")


# Exercise 3

# Swap two numbers

a = 10
b = 20

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")


# Exercise 4

# Find total marks

math = 90
science = 88
english = 91

total = math + science + english

print(total)


# Exercise 5

# Calculate average

average = total / 3

print(average)




# Code Challenge :

# Challenge 1

# Store

# Employee Name
# Company
# Experience
# Salary

# Print:

# Employee Rahul works at Microsoft.
# Experience: 4 Years
# Salary: $90000

employee_name = "Rahul"
company = "Microsoft"
experience = "4 Years"
salary = "$90000"

print(f"Employee {employee_name} works at {company}.")
print(f"Experience: {experience}")
print(f"Salary: {salary}")


# Challenge 2

# Store dimensions of a rectangle

# length = 20
# width = 15

# Calculate

# Area
# Perimeter

length = 20
width = 15

area = length * width
perimeter = 2 * (length + width)

print(f"Area of Rectangle = {area}")
print(f"Perimeter of Rectangle = {perimeter}")


# Challenge 3

# Store 5 subject marks.

# Calculate

# Total
# Average
# Percentage

english = 90
math = 88
marathi = 70
hindi = 80
science = 85

total = english + math + marathi + hindi + science
average = total / 5
percentage = total / 500 * 100

print(f"Total = {total}")
print(f"Average = {average}")
print(f"Percentage = {percentage}%")


# Challenge 4

# Store

# Product Name
# Price
# Quantity

# Calculate Total Bill.

product_name = "Laptop"
price = 799
quantity = 5

total_bill = price * quantity

print(f"Your Total Bill is ${total_bill}")


# Challenge 5

# Store

# Principal
# Rate
# Time

# Calculate Simple Interest.

# Formula

# SI = (P × R × T) / 100

principal_amount = 10000
rate_of_interest = 9
time_in_yrs = 2

simple_interest = principal_amount * rate_of_interest * time_in_yrs / 100

print(f"Simple Interest = {simple_interest}")