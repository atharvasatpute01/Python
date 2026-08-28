# 5. Join Sets

# Python provides several ways to sombine sets.

# union()
# Combines two sets and removes duplicates.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.union(b)

print(c)




# You can also use "|" :

c = a | b

print(c)




# update()
# Modifies the original set.

a = {1, 2, 3}
b = {4, 5, 6}

a.update(b)

print(a)