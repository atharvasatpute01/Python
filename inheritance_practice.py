# 1. Parent Class – Animal
# - Child Class: Dog
# - Method: eat()
# - Parent Parameters: name, colour
# - Child Parameter: breed

class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

class Dog(Animal):
    def __init__(self, name, colour, breed):
        super().__init__(name, colour)
        self.breed = breed

    def eat(self):
        print(self.name, "is eating")

dog1 = Dog("Luffy", "Golden", "Golden Retriever")

print("1).")
print("Name:",dog1.name)
print("Color:",dog1.colour)
print("Breed:",dog1.breed)

dog1.eat()





# 2. Parent Class – Employee
# - Child Class: Developer
# - Method: work()
# - Parent Parameters: emp_id, name
# - Child Parameter: programming_language

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

class Developer(Employee):
    def __init__(self, emp_id, name, programming_language):
        super().__init__(emp_id, name)
        self.programming_language = programming_language

    def work(self):
        print(self.name, "is Programming.")

dev1 = Developer(101, "Atharva", "Python")

print("\n2).")
print("Employee ID:", dev1.emp_id)
print("Employee Name:", dev1.name)
print("Programming Language:", dev1.programming_language)

dev1.work()





# 3. Parent Class – Mobile
# - Child Class: Smartphone
# - Method: make_call()
# - Parent Parameters: brand, model
# - Child Parameter: battery_capacity

class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Smartphone(Mobile):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def make_call(self):
        print("Calling using", self.brand, self.model)

M1 = Smartphone("Apple", "iPhone_18_pro", "5000mah")

print("\n3).")
print("Model:",M1.model)
print("Brand:",M1.brand)
print("Battery Capacity:",M1.battery_capacity)

M1.make_call()




# 4. Parent Class – BankAccount
# - Child Class: SavingsAccount
# - Method: display_balance()
# - Parent Parameters: account_holder, balance
# - Child Parameter: interest_rate

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate)

a1 = SavingsAccount("Atharva", 55000, 7)

print("\n4).")

a1.display_balance()





# 5. Parent Class – Laptop
# - Child Class: GamingLaptop
# - Method: run_game()
# - Parent Parameters: brand, processor
# - Child Parameter: graphics_card

class Laptop:
    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor

class GamingLaptop(Laptop):
    def __init__(self, brand, processor, graphics_card):
        super().__init__(brand, processor)
        self.graphics_card = graphics_card

    def run_game(self):
        print("Running game on", self.brand)


l1 = GamingLaptop("Lenovo", "Intel i7", "NVIDIA RTX 5060")

print("\n5).")

print("Brand:", l1.brand)
print("Processor:", l1.processor)
print("Graphics Card:", l1.graphics_card)

l1.run_game()





# Interest Rate:

P = 30000
r = 0.07
t = 5

A = P * ( 1 + r * t)

print("\nFinal Amount:", A)