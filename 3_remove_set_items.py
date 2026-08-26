# 3. Remove Set Items

# remove()
# Removes a specific item.

numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)

# If the item doesn't exist, remove() raises an error.




# discard()
# Also removes an item, but does not raise an error if the item doesn't exist.

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)


# Safe removal :

numbers.discard(100)

print(numbers)




# pop()
# Removes and returns an arbitrary element.

numbers = {10, 20, 30, 40}

x = numbers.pop()

print("Removed :", x)
print("Set :", numbers)

# Because sets are unordered, you should not assume which element will be removed.




# clear()
# Removes all elements.

numbers = {10, 20, 30, 40}

numbers.clear()

print(numbers)




# del 
# Deletes the entire set variable.

numbers = {10, 20, 30}

del numbers