# Example 1 – Animal Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()





# Explanation:
# - Animal is an abstract class.
# - sound() is an abstract method.
# - Dog and Cat provide their own implementations.
# - The abstract class defines what must be implemented, not how.