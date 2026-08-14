# *Remove List Items*

# Now  we'll learn how to remove items from a Python list.

# The four important ways are :

# remove()
# pop()
# del
# clear()




# 1. remove() – Remove by Value

# Use remove() when you know the value you want to delete.

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.remove("Banana")

print(fruits)

# Important :

# fruits.remove("Banana")

# means : Find "Banana" and remove it.

# You don't provide the index.




# 2. remove() with Duplicate Values

# If the same value appears multiple times :

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print(numbers)




# 3. pop() – Remove by Index

# pop() removes an item using its index.

cars = ["Mercedes", "Audi", "Volvo", "Toyota"]

cars.pop(1)

print(cars)




# 4. pop() Without an Index

# This is very important.

cars = ["Mercedes", "Audi", "Volvo", "Toyota"]

cars.pop()

print(cars)

# When you don't provide an index, pop() removes the last item.

# list.pop()

# → removes the last item.




# 5. pop() Returns the Removed Item

# One major advantage of pop() is that it gives you the removed value.

students = ["Amit", "Rahul", "Priya"]

removed_student = students.pop(1)

print("Removed :", removed_student)

print("Remaining :", students)

# This is useful when you need to use the deleted value later.




# 6. del – Delete Using Index

# del can also remove an item by index.

numbers = [10, 20, 30, 40, 50]

del numbers[2]

print(numbers)




# 7. del Can Remove Multiple Items

# You can combine del with slicing.

numbers = [10, 20, 30, 40, 50, 60]

del numbers[1:4]

print(numbers)




# 8. del Can Delete the Entire List

numbers = [10, 20, 30]

del numbers

# print(numbers) – commenting this out because this gives an error.

# This produces an error because the variable itself no longer exists.

# So :

# del numbers

# means : Delete the list variable completely.




# 9. clear() – Empty the List

# clear() removes all items, but the list itself remains.

numbers = [10, 20, 30, 40]

numbers.clear()

print(numbers)