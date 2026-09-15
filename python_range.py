# Python range

# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

# This set of numbers has its own data type called range.




# Creating ranges

# The range() function can be called with 1, 2, 3 arguments, using the syntax:

# range(start, stop, step)




# Call range() With One Argument

# If the range function is called with only one argument, the argument represents the stop value.

# The start argument is optional, and if not provided, it defaults to 0.

# range(10) returns a sequence of each number from 0 to 9. (The start argument, 0 is inclusive, and the stop argument, 10 is exculsive).




# Create a range of numbers from 0 to 9:

x = range(10)


# Create a range of numbers from 3 to 9:

x = range(3, 10)


# Create a range of numbers from 3 to 9:

x = range(3, 10, 2)


# Iterate over each value in a range:

for i in range(10):
    print(i)


# Convert different ranges to lists:

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))


# Extract a subsequence from a range:

r = range(10)

print(r[2])
print(r[:3])


# Test if the numbers 6 and 7 are present in a range:

r = range(0, 10, 2)

print(6 in r)
print(7 in r)


# Get the length of a range:

r = range(0, 10, 2)

print(len(r))