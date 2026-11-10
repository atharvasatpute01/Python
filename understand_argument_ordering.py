# 3. Understand argument ordering

# Python allows positional and keyword arguments together, but positional arguments must come first in a function call.

def calculate(a, b, c):
    print(a, b, c)
calculate(10, 20, c = 30)      # Correct

# Output:
# 10 20 30

# Incorrect:
# calculate(a = 10, 20, 30)     # SyntaxError

# Once you start supplying keyword arguments, you cannot follow them with ordinary positional arguments.