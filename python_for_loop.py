# Python for Loop

# A for loop is used to iterate over a sequence or collection

# Examples :

# List
# Tuple
# String
# Set
# Dictionary
# range()


# Basic Syntax :

# for variable in sequence:
#     statement


# Example with List

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)




# for Loop with range()

for i in range(1, 6):
    print(i)


# Remember :

# range(start, stop)

# The stop value is not included.

# So :
# range(1, 6)

# means :
# 1 2 3 4 5 




# Nested for - Multiplication Table

for i in range(1, 6):
    for j in range(1, 11):
        print(i * j)
    print()




# Nested for - Pattern

# Nested loops are commonly used for patterns.

# Square Pattern

for i in range(5):
    for j in range(5):
        print("*", end = "")
    print()




# Very Important Example - Student Marks

students = [
    [80, 75, 90],
    [65, 70, 72],
    [95, 88, 91]
]

for student in students:

    for marks in student:

        if marks >= 75:
            print(marks, "Good")
        else:
            print(marks, "Needs Improvement")