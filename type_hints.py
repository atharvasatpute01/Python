# 1. Type hints

# Type hints tell us what type of value a function is expected to receive and return.

# Example 1: Without type hints

def add(a, b):
    return a + b
print(add(10, 20))

# Example 2: With typpe hints

def add(a : int, b: int) -> int:
    return a + b
print(add(10, 20))

# Real-world example: Calculate an employee's annual salary

def annual_salary(monthly_salary: float) -> float:
    return monthly_salary * 12

salary = annual_salary(50000.0)
print(salary)