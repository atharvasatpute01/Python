# Loop Lists

# How to process every item in a list automatically.

# The main ways are :

# for loop
# for loop with index
# range()
# enumerate()
# while loop




# Practical list-processing programs

# 1. Basic for Loop

# To print every student :

students = ["Amit", "Rahul", "Priya", "Neha"]

for student in students:
    print(student)

# How it works :

# First iteration → Amit
# Second iteration → Rahul
# Third iteration → Priya
# Fourth iteration → Neha

# Python automatically takes each item from the list.




# 2. for Loop with a Condition

# We can combine a loop with if.

marks = [35, 78, 45, 90, 32, 65]

for mark in marks:
    if mark >= 40:
        print(mark, "Pass")




# 3. Print Only Even Numbers

numbers = [10, 15, 20, 25, 30, 35, 40]

for number in numbers:
    if number % 2 == 0:
        print(number)




# 4. Print Only Odd Numbers

# numbers = [10, 15, 20, 25, 30, 35, 40]

for number in numbers:
    if number % 2 != 0:
        print(number)




# 5. Using range() with a List

# We can use indexes with range().

students = ["Amit", "Rahul", "Priya", "Neha"]

for i in range(len(students)):
    print(students[i])




# 6. Print Index and Value

# A very useful technique :

students = ["Amit", "Rahul", "Priya", "Neha"]

for i in range(len(students)):
    print(i, students[i])




# 7. Using enumerate()

# Python provides a cleaner way to get both the index and value.

students = ["Amit", "Rahul", "Priya", "Neha"]

for index, student in enumerate(students):
    print(index, student)




# 8. Start enumerate() from 1

# By default, enumerate() starts at 0.

# You can change it :

students = ["Amit", "Rahul", "Priya", "Neha"]

for number, student in enumerate(students, start=1):
    print(number, student)




# 9. while Loop with a list

# We can also loop through a list using while.

students = ["Amit", "Rahul", "Priya", "Neha"]

i = 0

while i < len(students):
    print(students[i])
    i += 1




# 10. for vs while

# for loop :

# Use it when you simply want to process each item.

for student in students:
    print(student)

# while loop :

# Useful when the loop depends on a condition.

i = 0

while i < len(students):
    print(students[i])
    i += 1

# For normal list traversal, for is generally simpler.




# 11. Loop Through a List and Search

students = ["Amit", "Rahul", "Priya", "Neha"]

search_name = "Priya"

for student in students:
    if student == search_name:
        print("Student Found")




# 12. Search with in

# Even simpler :

students = ["Amit", "Rahul", "Priya", "Neha"]

if "Priya" in students:
    print("Student Found")
else:
    print("Student Not Found")