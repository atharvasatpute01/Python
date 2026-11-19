# A. Public Variables

class Student:

    def __init__(self):
        self.name = "Rahul"
        self.age = 22

student = Student()

print(student.name)
print(student.age)

student.name = "Amit"

print(student.name)