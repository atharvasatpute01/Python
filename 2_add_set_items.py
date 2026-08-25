# 2. Add Set Items :

# add()
# Adds one item to a set.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)




# Adding a duplicate

numbers = {10, 20, 30}

numbers.add(20)

print(numbers)




# update()
# Adds multiple items.

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)


# You can also use another set :

a = {10, 20, 30}
b = {40, 50, 60}

a.update(b)

print(a)