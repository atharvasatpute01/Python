# List Comprehension

# List comprehension is one of the most important Python concepts for data analysis, automation, and interviews.

# It allows us to create a new list using a compact syntax




# 1. Normal for Loop

# Suppose we want squares of numbers :

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)




# 2. Same Proogram Using List Comprehension

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)




# 3. Double Every Number

numbers = [10, 20, 30, 40]

result = [number * 2 for number in numbers]

print(result)




# 4. Add 10 to Every Number

numbers = [10, 20, 30, 40]

result = [number + 10 for number in numbers]

print(result)




# 5. List Comprehension with if

# eg.1

numbers = [10, 15, 20, 25, 30, 35]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# eg.2

marks = [35, 78, 42, 91, 28]

result = ["Pass" if mark >= 40 else "Fail" for mark in marks]

print(result)




# 6. Nested List Comprehension

# You can use a list comprehension inside another list comprehension.

# Example :

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [number for row in matrix for number in row]

print(result)




# ** List Comprehension Cheat Sheet **

# Basic
# [new_value for item in list]

# With Condition
# [item for item in list if condition]

# With transformation
# [item * 2 for item in numbers]

# With if-else
# ["Pass" if mark >= 40 else "Fail"for mark in marks]

# With range()
# [number ** 2 for number in range(1, 11)]

# String transformation
# [name.upper() for name in names]

# Filtering strings
# [name for name in names if name.startswith("A")]