# 1. Positional-only parameters (/)

# A parameter before / must be passed by position, not by its name.

def student(name, /):
    print(name)
student("Rahul")

# Why? The / symbol tells Python that name is positional-only.