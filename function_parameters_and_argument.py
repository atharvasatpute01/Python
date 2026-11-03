# Python Function Parameters and Arguments

def add(a, b):       # a and b are parameters
    print(a + b)

add(10, 20)          # 10 and 20 are arguments

# Parameter: A variable written inside the function defination (a, b).

# Argument: The actual value passed when calling the function (10, 20).





# 1. Positional arguments

# Values are assigned according to their position.

def student(name, age):
    print(name)
    print(age)

student("Rahul", 21)





# 2. Keyword arguments

# Values are assigned using parameter names.

def student(name, age):
    print(name, age)

student(age = 21, name = "Rahul")





# 3. Default arguments

# A parameter has a default value if no arguments is supplied.

def greet(name = "Guest"):
    print("Hello", name)

greet()
greet("Rahul")





# 4. *args

# Use *args when you want to pass any number of positional arguments.

# def add(*nums):
#     print(nums)

# add(10, 20, 30, 40)


# def add(nums):
#     print(nums)

# add(10, 20, 30, 40)


# Example of adding the values:

def add(*nums):
    total = 0

    for num in nums:
        total += num
    print(total)

add(10, 20, 30)





# 5. ** kwargs

# Use **kwargs to accept any number of keyword arguments.

def show(**data):
    print(data)

show(name = "Raj", age = 22, city = "Pune")





# 6. Keyword-only parameter

# Parameter written after * must be passed using their names.

def greet(*, name):
    print("Hello", name)

greet(name = "Raj")          # Correct





# 7. Type hints

# Type hints document the expected types of inputs and outputs.

def add(a: int, b = int) -> int:
    return a + b
print(add(10, 20))

# Here, int indicates the expected integer type, and -> int indicates the expected return type. Python generally does not enforce these hints automatically.





# 8. Unpacking with *

# Unpacking passes the elements of a sequence as separate arguments.

def add(a, b):
    print(a + b)
nums = [10, 20]
add(*nums)


# add(*nums) is equivalentto add (10, 20).





# 9. Dictionary Unpacking with **

# Unpacking a dictionary passes its entries as keyword arguments.

def show(name, age):
    print(name, age)
data = {"name": "Raj", "age": 22}
show(**data)

# The dictionary keys must match the function's parameter names, unless the function accepts extra keyword arguments.