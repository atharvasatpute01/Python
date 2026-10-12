# Positive, Negative or Zero

def check_number(number):

    if number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"

    else:
        return "Zero"


print(check_number(10))
print(check_number(-5))
print(check_number(0))