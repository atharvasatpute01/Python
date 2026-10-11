# Function creation
def my_function():
    print("Hello from a function")

# Function call
my_function()





# You can call the same function multiple times:

# Example

def my_function():
    print("Hello from a function")

my_function()
my_function()
my_function()





# Function Names:
# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (muFunction and myfunction are different)

# Example

# Valid function names:

# calculate_sum()
# _private_function()
# myFunction2()





# Why Use Functions?

# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculations code repeatedly:

# Example

# Without functions - repetitive code:

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


# With functions - reusable code:

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))





# Return Values

# Functions can send data back to the code that called them using the return sstatement.

# When a function reaches a return statement, it stops executing and sends the result back:

# Example

# A function that returns a value:

def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)


# Using the return value directly:

def get_greeting():
    return "Hello from a function"

print(get_greeting())





# The pass Statement

# Function defitions cannot be empty. if you need to create a function placeholder without any code, use the pass statement:

# Example

def my_function():
    pass