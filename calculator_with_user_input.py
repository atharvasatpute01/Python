# Calculator With User Input

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition: ", add(a, b))
print("Substration: ", substract(a, b))
print("Multiplication: ", multiply(a, b))
print("Divide: ", divide(a, b))