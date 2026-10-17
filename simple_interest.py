# SI = (P * T * R) / 100

def simple_interest(principal, roi, time):
    return (principal * roi * time) / 100

print(simple_interest(1000, 9, 1))