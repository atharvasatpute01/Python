# Complete Set Example

students_python = {
    "Amit",
    "Rahul",
    "Priya",
    "Sneha"
}


students_sql = {
    "Priya",
    "Sneha",
    "Karan",
    "Amit"
}


print("Python Students:")
print(students_python)


print("\nSQL Students:")
print(students_sql)


print("\nStudents learning both:")
print(students_python & students_sql)


print("\nOnly Python:")
print(students_python - students_sql)


print("\nOnly SQL:")
print(students_sql - students_python)


print("\nAll Students:")
print(students_python | students_sql)


print("\nStudents in exactly one course:")
print(students_python ^ students_sql)