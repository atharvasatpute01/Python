# *Hands-On Practice*

# Use this list for Questions 1–5:

# cities = [
#     "Mumbai",
#     "Pune",
#     "Delhi",
#     "Bangalore",
#     "Chennai",
#     "Hyderabad",
#     "Kolkata"
# ]
# Question 1

# Display: Mumbai, Bangalore, Kolkata

# using indexing.

cities = ["Mumbai", "Pune", "Delhi", "Bangalore", "Chennai", "Hyderabad", "Kolkata"]

print(cities[0])
print(cities[3])
print(cities[6])




# Question 2

# Display the last city using negative indexing.

# Expected:

# Kolkata

print(cities[-1])





# Question 3

# Display:

# ['Pune', 'Delhi', 'Bangalore']

# using slicing.

print(cities[1:4])




# Question 4

# Display the first four cities.

# Expected:

# ['Mumbai', 'Pune', 'Delhi', 'Bangalore']

print(cities[:4])




# Question 5

# Display all cities starting from "Bangalore" until the end.

# Expected:

# ['Bangalore', 'Chennai', 'Hyderabad', 'Kolkata']

print(cities[3:])




# Question 6

# Given:

# marks = [55, 67, 78, 82, 91, 73, 66, 88]

# Write slicing statements to display:

# First 3 marks
# Last 3 marks
# Marks from index 2 to 5
# Every second mark

marks = [55, 67, 78, 82, 91, 73, 66, 88]

print(marks[0:3])
print(marks[-3:])
print(marks[1:5])
print(marks[::2])