# 6. Intersection

# Finds elements that exxist in both sets.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.intersection(b)

print(result)




# Using "&" :

result = a & b

print(result)




# Real-world example :

python_students = {"Amit", "Rahul", "Priya", "Sneha"}

sql_students = {"Priya", "Sneha", "Karan", "Amit"}

both = python_students & sql_students

print("Student learning both :")
print(both)