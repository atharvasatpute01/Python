# Packing
person = ("Alice", 25, "Engineer")

# Unpacking
name, age, job = person
 
print(name)   # Alice
print(age)    # 25
print(job)    # Engineer


# Using * for multiple values :

numbers = (1, 2, 3, 4, 5)

a, *b, c = numbers

print(a)   # 1
print(b)   # [2, 3, 4]
print(c)   # 5