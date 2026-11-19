class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
            return self.__marks
    
    def set_marks(self, value):
        if 0 <= value <= 100:
             self.__marks = value
        else:
            print("Invalid Marks")

stud = Student(90)

print("Marks:", stud.get_marks())

stud.set_marks(95)

print("Updated Salary:", stud.get_marks())

stud.set_marks(101)