# Python match

# Python's match statement is useful when we need to compare one value against multiple possible patterns/values.

# It is similar to switch in languages such as C, C++, Java and JavaScript.

# Basic Syntax :

# match value:
#     case value1:
#         statement
#     case value2:
#         statement
#     case _:
#         statement


day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")


# case _

# _ works as the default case.

choice = 5

match choice:
    case 1:
        print("Add")
    case 2:
        print("Update")
    case 3:
        print("Delete")
    case _:
        print("Invalid choice")