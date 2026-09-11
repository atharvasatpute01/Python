# Nested if

# A nested if means putting one if statement inside another if statement.

# Basic Syntax
# if condition1:
#     if condition2:
#         statement

# The inner if is checked only when the outer if is True.


# Example : Age and Citizenship

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")




# Nested if with else

age = 20
citizen = False

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen")
else:
    print("You are under 18")