# Python String Formatting

# F-Strings:

# F-string allows you to format selected parts of a string.

# To specify a string as an f-string, simply put an f in front of the string lterals, like this:

# Create am f-string:

txt = f"The price is 49 dollars"

print(txt)




# Add a placeholder for the price variable:

price = 59
txt = f"the price is {price} dollars"

print(txt)




# Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"

print(txt)




# Display the value 95 with 2 decimals:

txt = f"The price is {95:.2f} dollars"

print(txt)




# Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"

print(txt)




# Add taxes before displaying the price:

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"

print(txt)




price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"

print(txt)




# Use the string method upper()to convert a value into upper case letters:

fruit = "apples"
txt = f"I love {fruit.upper()}"

print(txt)




# Use a comma as a thousand separator:

price = 59000
txt = f"The price is {price:,} dollars"

print(txt)




# Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"

print(txt.format(price))




# Format the price to be displayed as a number with two decimals:

txt = "The price is {:.2f} dollars"




# Multiple Values

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."

print(myorder.format(quantity, itemno, price))




# Index Numbers

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."

print(myorder.format(quantity, itemno, price))




# if you want to refer to the same values more then once, use the index number:

# Example
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."

print(txt.format(age, name))




# Named Indexes

myorder = "I have a {carname}, it is a {model}."

print(myorder.format(carname = "Ford", model = "Mustang"))