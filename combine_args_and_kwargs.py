# 4. Combine *args and **kwargs

# You can accept both extra positional and extra keyword arguments in the same function.

def demo(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
demo(10, 20, 30, name = "Rahul", age = 22)

# Here:

# - args stores extra positional values in a tuple.
# - kwargs stores extra keyword values in a dictionary.

# This pattern is useful when building flexible functions, reusable utilities, and API wrappers.