# Encapsulation Using @property
# Python provides @property and setter decorators for controlled attribute access.

class Student:

    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid Marks")

s = Student(80)

print(s.marks)

s.marks = 95

print(s.marks)

s.marks = 150
