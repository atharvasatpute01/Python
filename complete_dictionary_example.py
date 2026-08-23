# ==========================================
# PYTHON DICTIONARY - COMPLETE EXAMPLE
# ==========================================

# Creating a Dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "BCA",
    "marks": 85
}

print("Original Dictionary :")
print(student)


# ==========================================
# 1. ACCESS ITEMS
# ==========================================

print("\n--- 1. Access Items ---")

print("Name :", student["name"])
print("Age :", student["age"])

# Using get()
print("Course :", student.get("course"))


# ==========================================
# 2. CHANGE ITEMS
# ==========================================

print("\n--- 2. Change Items ---")

student["age"] = 22
student["marks"] = 90

print("Updated Dictionary :")
print(student)


# ==========================================
# 3. ADD ITEMS
# ==========================================

print("\n--- 3. Add Items ---")

student["city"] = "Mumbai"
student["college"] = "ABC College"

print("After Addding Items :")
print(student)


# ==========================================
# 4. REMOVE ITEMS
# ==========================================

print("\n--- 4. Remove Items ---")

# Remove a specific item
student.pop("city")

print("After pop() :")
print(student)

# Remove another item
del student["college"]

print("After del :")
print(student)


# ==========================================
# 5. LOOP DICTIONARIES
# ==========================================

print("\n--- 5. Loop Dictionaries ---")

# Loop through keys
for key in student:
    print(key)

print("\nKeys and Values :")

# Loop through keys and values
for key, value in student.items():
    print(key, ":", value)


# ==========================================
# 6. COPY DICTIONARIES
# ==========================================

print("\n--- 6. Copy Dictionaries ---")

student_copy = student.copy()

print("Original Dictionary :")
print(student)

print("Copied Dictionary :")
print(student_copy)


# ==========================================
# 7. NESTED DICTIONARIES
# ==========================================

print("\n--- 7. Nested Dictionaries ---")

students = {
    "student1": {
        "name": "Rahul",
        "age": 21,
        "marks": 90
    },

    "student2": {
        "name": "Priya",
        "age": 20,
        "marks": 95
    },

    "student3": {
        "name": "Amit",
        "age": 22,
        "marks": 88
    }
}

print(students)

print("\nStudent 1 Name :")
print(students["student1"]["name"])

print("\nStudent 2 Marks :")
print(students["student2"]["marks"])


# ==========================================
# 8. DICTIONARY METHODS
# ==========================================

print("\n--- 8. Dictionary Methods ---")

data = {
    "name": "Sneha",
    "age": 21,
    "course": "MCA",
    "marks": 92
}

# keys()
print("Keys :")
print(data.keys())

# values()
print("\nValues :")
print(data.values())

# items()
print("\nItems :")
print(data.items())

# get()
print("\nGet Name :")
print(data.get("name"))

# update()
data.update({"marks": 95})
print("\nAfter update() :")
print(data)

# pop()
data.pop("age")
print("\nAfter pop() :")
print(data)

# setdefault()
data.setdefault("city", "Pune")
print("\nAfter setdefault() :")
print(data)


# ==========================================
# FINAL DICTIONARY
# ==========================================

print("\n--- Final Dictionary ---")