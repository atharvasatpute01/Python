# class : Blueprint for creating objects
class Student:
    name = "Atharva"
    def show(self):
        return self.name





# Object : Instance of a class
class Student:
    name = "Atharva"
    def show(self):
        return self.name
s1 = Student()
print(s1.show())        





# Constructor : Initializes an object
class Student:
    def __init__(self):
        self.name = "Atharva Satpute"
    def show(self):
        return self.name
S1 = Student()
print(S1.show())        





# Encapsulation : Bundles data and methods
class Student:
    def __init__(self):
        self.__age = 20
    def show(self):
        return self.__age

s1 = Student()
print(s1.show())





# Inheritance : Reuses parent-class functionality
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()
d.bark()





# Polymorphism : Same interface, different behaviour
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()





# Abstraction : Hides implementation details
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

c = Car()
c.start()





# class method: Works with class-level data
class Student:
    school = "ABC School"

    @classmethod
    def show(cls):
        return cls.school

print(Student.show())





# Static method: Utility method associated with a class
class Student:

    @staticmethod
    def add(a, b):
        return a + b

print(Student.add(10, 20))