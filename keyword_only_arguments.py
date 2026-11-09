# 2. Keyword-only parameters (*)

# A parameter after * must be passed using its name.

def employee(*, name, salary):
    print(name, salary)
employee(name = "Amit", salary = 50000)      # Corrrect

# This is incorrect:
# employee("Amit", 50000)      # Error

# Remember:

# - / means positional-only.
# - * means keyword-only for parameters following it.