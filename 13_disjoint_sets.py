# 13. Disjoint Sets

# Two sets are disjoint when they have no common elements.

a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))

# Output:

# True




# Example with common elements:

a = {1, 2, 3}
b = {3, 4, 5}

print(a.isdisjoint(b))

# Output:

# False