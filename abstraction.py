# *Python OOP – Abstraction*
# Abstraction is the fourth pillar of Object-Oriented Programming (OOP).
# 1. What is Abstraction?
# Abstraction means hiding internal implementation details and showing only the essential functionality to the user.

# In simple words:
# - Show what an object does.
# - Hide how the object does it.
# - Focus on functionality rather than internal implementation.

# When you use an ATM:
# 1. Insert your card.
# 2. Enter your PIN.
# 3. Select withdrawal.
# 4. Enter the amount.
# 5. Collect your cash.
# You don't need to know how the ATM communicates with the bank server or verifies your account internally.

# This is abstraction.


# 2. How to Implement Abstraction in Python?
# Python provides the abc module.

# abc stands for Abstract Base Classes.

# We mainly use:
# - ABC – Creates an abstract base class.
# - @abstractmethod – Declares a method that child classes must implement.


# Basic syntax

from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def method_name(self):
        pass


class Child(Parent):

    def method_name(self):
        print("Method Implemented")


obj = Child()
obj.method_name()

# Important: You cannot create an object of a class that still has unimplemented abstract methods.