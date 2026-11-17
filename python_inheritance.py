# What Is Inheritance in Python?
# Inheritance is an Object-Oriented Programming (OOP) concept that allows one class to acquire the properties and methods of another class.


# It promotes:
# - Code reusability
# - Reduced code duplication
# - Easy maintenance
# - Better code organization
# - Extensibility


# Real-Life Example
# Consider a company with different types of employees.
# - Employee is the parent class.
# - Developer is a child class.
# - DataAnalyst is another child class.
# Both developers and data analysts share common employee properties, such as name and salary, but they can also have their own specific methods.


# Single Inheritance
# Definition: When a child class inherits from a single parent class, it is called single inheritance.

# Example 1: Student Management System

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display_person()
        print("Course:", self.course)


# Creating an object
s1 = Student("Rahul", 22, "Data Science")

s1.display_student()

# Explanation

# Parent class: Person
# - Stores the student's name and age.
# - Defines the display_person() method.

# Child class: Student
# - Inherits from Person.
# - Adds the course attribute.
# - Uses the inherited method display_person().

# What Is super()?
# The super() function allows a child class to access methods from its parent class.

# This calls the constructor of the parent class and initializes name and age.

# Important: Without this call, the parent constructor would not automatically execute in this example, because the child class defines its own __init__() method.




# Multiple Inheritance

# Definition: When a child class inherits from two or more parent classes, it is called multiple inheritance.

# Example 2: Employee with Technical and Management Skills

class TechnicalSkills:
    def coding(self):
        print("\nEmployee can write Python code.")


class ManagementSkills:
    def manage_team(self):
        print("Employee can manage a team.")


class TeamLead(TechnicalSkills, ManagementSkills):
    def lead_project(self):
        print("Employee leads a software project.")


# Creating an object
t1 = TeamLead()

t1.coding()
t1.manage_team()
t1.lead_project()