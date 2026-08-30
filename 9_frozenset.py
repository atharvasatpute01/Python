# 9. Frozenset

# A frozenset is an immutable set.

# Once created, you cannot add or remove elements.

numbers = frozenset([10, 20, 30, 40])

print(numbers)
print(type(numbers))


# This will cause an error:

# numbers.add(50)

# because a frozenset cannot be modified.

# Why use frozenset?

# Use it when you need a set whose contents must not change.