# 1. Access Set Items

# Sets are unordered, so you cannot access elements using an index.


# This is not allowed :
numbers = {10, 20, 30, 40}

print(numbers[0])


# Instead, use a loop :
numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)




# Check whether an item exists :

numbers = {10, 20, 30, 40}

# in
if 20 in numbers:
    print("20 is present")


# not in
if 50 not in numbers:
    print("50 is not present")