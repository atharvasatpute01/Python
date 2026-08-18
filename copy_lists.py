# 1. The Problem with list2 = list1

# Consider :

list1 = ["Python", "SQL", "Excel"]

list2 = list1

print(list1)
print(list2)

# Output :

# ['Python', 'SQL', 'Excel']
# ['Python', 'SQL', 'Excel']

# It looks like we copied the list.

# But let's modify list2:

list1 = ["Python", "SQL", "Excel"]

list2 = list1

list2.append("Power BI")

print("List 1 :", list1)
print("List 2 :", list2)

# Output :

# List 1: ['Python', 'SQL', 'Excel', 'Power BI']
# List 2: ['Python', 'SQL', 'Excel', 'Power BI']

# Why?

# Because :

list2 = list1

# Doesn't create a new list.

# Both variables refer to the same list object.