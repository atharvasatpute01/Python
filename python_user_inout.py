# Python User Input

# User Input
# Python allows for user input.

# That means we are able to ask the user for input.

# Ask for user input:

print("Enter your name:")
name = input()
print(f"Hello {name}")





# Using Prompt

# Add a message in front of the user input:

name = input("Enter your name:")
print(f"Hello {name}")





# Multiple Inputs

name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favourite animal:")
fav2 = input("What is your favourite color:")
fav3 = input("What is your favourite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")





# Input Number

# To find the square root, the input has to be converted into a number:

x = input("Enter a number:")

# find the square root of the number:

import math
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")





# Validate Input

# Keep asking until you get a number:

y = True

while y == True:
    x = input("Enter a number:")
    try:
        x = float(x);
        y = False
    except:
        print("Wrong input, please try again.")

print("Thank you!")