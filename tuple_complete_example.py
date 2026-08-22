# ==========================================
# PYTHON TUPLES - COMPLETE EXAMPLE
# ==========================================

# Creating Tuples
student = ("Rahul", 21, "BCA", 85)

print("Original Tuple :")
print(student)


# ==========================================
# 1. ACCESS TUPLES
# ==========================================

print("\n--- 1. Access Tuples ---")

print("Name :", student[0])
print("Age :", student[1])
print("Course :", student[2])
print("Marks :", student[3])

# Negative indexing
print("Last Item :", student[-1])


# ==========================================
# 2. UPDATE TUPLES
# ==========================================

print("\n--- 2. Update Tuples ---")

# Tuples cannot be directly changed.
# Convert Tuple -> List -> Update -> Tuple

student_list = list(student)

student_list[1] = 22
student_list[3] = 90

student = tuple(student_list)

print("Updated Tuple :")
print(student)


# ==========================================
# 3. UNPACK TUPLES
# ==========================================

print("\n--- 3. Unpack Tuples ---")

name, age, course, marks = student

print("Name :", name)
print("Age :", age)
print("Course :", course)
print("Marks :", marks)


# ==========================================
# 4. LOOP TUPLES
# ==========================================

print("\n--- 4. Loop Tuples ---")

for item in student:
    print(item)


# Loop with index
print("\nTuple with Index :")

for index, item in enumerate(student):
    print(index, ":", item)


# ==========================================
# 5. JOIN TUPLES
# ==========================================

print("\n--- 5. Join Tuples ---")

tuple1 = ("Python", "SQL")
tuple2 = ("Power BI", "Excel")

joined_tuple = tuple1 + tuple2

print("Tuple 1 :", tuple1)
print("Tuple 2 :", tuple2)
print("Joined Tuple :", joined_tuple)


# ==========================================
# 6. TUPLE METHODS
# ==========================================

print("\n--- 6. Tuple Methods ---")

numbers = (10, 20, 20, 30, 20, 40)

# count()
print("Tuple :", numbers)
print("Count of 20 :", numbers.count(20))

# index()
print("Index of 30 :", numbers.index(30))


# ==========================================
# FINAL OUTPUT
# ==========================================

print("\n--- Final Student Information ---")

print("Name :", student[0])
print("Age :", student[1])
print("Course :", student[2])
print("Marks :", student[3])