def calculation_sub(n):
    total = 0

    for i in range(1, n + 1):
        total = total - i

    return total

print(calculation_sub(10))