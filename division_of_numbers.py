def calculation_div(n):
    total = n

    for i in range(1, n + 1):
        total = total / i

    return total

print(calculation_div(10))