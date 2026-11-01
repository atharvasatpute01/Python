# 1. Built-in Python Functions

# These functions are already available in Python. You do not need to define them yourself.


# print()
print("Hello Python")


# input()
name = input("Enter your name: ")
print(name)


# type()
print(type(10))


# int()
print(int("25"))


# float()
print(float("3.14"))


# str()
print(str(100))


# bool()
print(bool(1))


# len()
print(len("Python"))


# range()
print(list(range(1, 6)))


# sum()
print(sum([10, 20, 30]))


# min()
print(min([5, 2, 8]))


# max()
print(max([5, 2, 8]))


# abs()
print(abs(-15))


# round()
print(round(3.14159, 2))


# pow()
print(pow(2, 3))


# divmod()
print(divmod(10, 3))


# sorted()
print(sorted([3, 1, 2]))


# reversed()
print(list(reversed([1, 2, 3])))


# enumerate()
print(list(enumerate(["A", "B"])))


# zip()
print(list(zip([1, 2], ["A", "B"])))


# all()
print(all([True, True]))


# any()
print(any([False, True]))


# isinstance()
print(isinstance(10, int))


# id()
x = 100
print(id(x))


# help()
help(len)





# 2. Basic Function Syntax


# Define a function
# def name():
def greet():
    print("Hello, Atharva")


# Call a function
# name()
greet()


# Function with parameter
# def name(x):
def greet_name(name):
    print("Hello", name)

greet_name("Atharva")


# Return a value
# return value
def multiply(a, b):
    return a * b

print(multiply(5, 5))


# Function with two parameter
# def name(a, b)
def add(a, b):
    return a + b

print(add(4, 7))


# Default parameter
# def name(x = 10):
def greet_admin(name="Atharva"):
    print("Hello", name)

greet_admin()


# Multiply parameters
# def name(*args):


# Keyword arguments
# def name(**kwrgs):


# One-line function
# lambda x: expression


# Documentation string
# """Description"""





# 6. String Methods Often Used Inside Functions


# upper()
# Convert to uppercase
text = "python"
print(text.upper())


# lower()
# Convert to lowercase
text = "PYTHON"
print(text.lower())


# title()
# Capitalize each word
print("hello world".title())


# capitalize()
# Capitalize the first character
print("python programming".capitalize())


# strip()
# Remove surrounding whitespace
print("  hello  ".strip())


# replace()
# Replace text
print("cat".replace("c", "b"))


# split()
# Split a string into a list
print("a,b,c".split(","))


# join()
# Join strings
print("-".join(["a", "b"]))


# find()
# Find a substring position
print("python".find("th"))


# startswith()
# Check starting text
print("python".startswith("py"))


# endswith()
# Check ending text
print("file.csv".endswith("csv"))


# count()
# Count occurrences
print("banana".count("a"))





# 7. List, Dictionary and Set Methods


# List

# append()
# Add one item to the end
nums = [1, 2, 3]
nums.append(10)
print(nums)


# extend()
# Add multiple items
nums = [1, 2, 3]
nums.extend([20, 30])
print(nums)


# insert()
# Insert an item at a specific position
nums = [10, 20, 30]
nums.insert(0, 5)
print(nums)


# remove()
# Remove a specific item
nums = [10, 20, 30]
nums.remove(10)
print(nums)


# pop()
# Remove an item by index
nums = [10, 20, 30]
nums.pop()
print(nums)


# sort()
# Sort items in ascending order
nums = [30, 10, 20, 5]
nums.sort()
print(nums)


# reverse()
# Reverse the list
nums = [10, 20, 30]
nums.reverse()
print(nums)


# Dictionary

data = {
    "name": "Atharva",
    "age": 21,
    "course": "Python"
}


# keys()
# Display all keys
print(data.keys())


# values()
# Display all values
print(data.values())


# items()
# Display keys and values
print(data.items())


# get()
# Get a value using a key
print(data.get("name", "Unknown"))


# update()
# Add or update dictionary values
data.update({"age": 25})
print(data)


# Set

# add()
# Add an item to a set
items = {1, 2, 3}
items.add(10)
print(items)


# discard()
# Remove an item if it exists
items = {1, 2, 3}
items.discard(2)
print(items)


# union()
# Combine two sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))


# intersection()
# Find common items
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))