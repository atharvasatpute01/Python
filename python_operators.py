# ==========================================================
#               PYTHON OPERATORS - FULL PROGRAM
# ==========================================================


print("=" * 60)
print("                      PYTHON OPERATORS")
print("=" * 60)


# ==========================================================
# 1. ARITHMETIC OPERATORS
# ==========================================================


print("\n1.ARITHMETIC OPERATORS")
print("-" * 60)

a = 20
b = 6

print("a =", a)
print("b =", b)

print("Addition       :", a + b)
print("Substraction   :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Modulus        :", a % b)
print("Floor Division :", a // b)
print("Exponent       :", a ** b)


# ==========================================================
# 2. ASSIGNMENT OPERATORS
# ==========================================================


print("\n2.ASSIGNMENT OPERATORS")
print("-" * 60)

x = 10
print("Initial x =", x)

x += 5
print("x += 5 :", x)

x -= 3
print("x -= 3  :", x)

x *= 2
print("x *= 2  :", x)

x /= 4
print("x /= 4  :", x)

x %= 5
print("x %= 5  :", x)

x = 20
x //= 3
print("20 //= 3:", x)

x = 5
x **= 2
print("5 **= 2 :", x)


# ==========================================================
# 3. TERNARY OPERATOR
# ==========================================================


print("\n3. TERNARY OPERATOR")
print("-" * 60)

age = 20

result = "Adult" if age >= 18 else "Minor"

print("Age    :", age)
print("Result :", result)

marks = 75

result = "Pass" if marks >= 40 else "Fail"

print("Marks :", marks)
print("Result :", result)


# ==========================================================
# 4. COMPARISON OPERATORS
# ==========================================================


print("\n4. COMPARISON OPERATORS")
print("-" * 60)

a = 10
b = 20

print("a =", a)
print("b =", b)

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)


# ==========================================================
# 5. LOGICAL OPERATORS
# ==========================================================


print("\n5. LOGICAL OPERATORS")
print("-" * 60)

age = 25
salary = 50000

print("Age :", age)
print("Salary :", salary)

print("AND :", age >= 18 and salary >= 30000)

print("OR :", age >= 18 or salary >= 60000)

print("NOT :", not age >= 18)


# Another Logical Operator Example

username = "admin"
password = "1234"

login = username == "admin" and password == "1234"

print("\nLogin Successful :", login)


# ==========================================================
# 6. IDENTITY OPERATORS
# ==========================================================


print("\n6. IDENTITY OPERATORS")
print("-" * 60)

list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("list1 =", list1)
print("list2 =", list2)
print("list3 =", list3)

print("\nlist1 == list2 :", list1 == list2)
print("list1 is list2 :", list1 is list2)

print("\nlist1 == list3 :", list1 == list3)
print("list1 is list3 :", list1 is list3)

print("\nlist1 is not list3 :", list1 is not list3)


# ==========================================================
# 7. MEMBERSHIP OPERATORS
# ==========================================================


print("\n7. MEMBERSHIP OPERATORS")
print("-" * 60)

courses = [
    "Python",
    "SQL",
    "Power BI",
    "AWS",
    "Cyber Security"
]

print("Courses :", courses)

print("Python in courses   :", "Python" in courses)
print("Java in courses     :", "Java" in courses)
print("Java not in courses :", "Java" not in courses)


# Membership Operator With String

company = "Syntova AI"

print("\nCompany :", company)

print("'AI' in company     :", "AI" in company)
print("'Java' in company   :", "Java" in company)


# ==========================================================
# 8. BITWISE OPERATORS
# ==========================================================


print("\n8. BITWISE OPERATORS")
print("-" * 60)

a = 5
b = 3

print("a =", a)
print("b =", b)

print("\nBinary of a :", bin(a))
print("Binary of b :", bin(b))

print("\na & b  :", a & b)
print("a | b  :", a | b)
print("a ^ b  :", a ^ b)
print("~a     :", ~a)
print("a << 1 :", a << 1)
print("a >> 1 :", a >> 1)


# ==========================================================
# 9. OPERATOR PRECEDENCE
# ==========================================================


print("\n9. OPERATOR PRECEDENCE")
print("-" * 60)

result1 = 10 + 5 * 2

result2 = (10 + 5) * 2

result3 = 2 ** 3 * 4

result4 = 100 / 10 + 5

print("10 + 5 * 2    =", result1)

print("(10 + 5) * 2  =", result2)

print("2 ** 3 * 4    =", result3)

print("100 / 10 + 5  =", result4)


# ==========================================================
# 10. PRACTICAL EXAMPLE - EVEN OR ODD
# ==========================================================


print("\n10. EVEN OR ODD")
print("-" * 60)

number = 25

result = "Even" if number % 2 == 0 else "Odd"

print("Number :", number)
print("Result :", result)


# ==========================================================
# 11. PRACTICAL EXAMPLE - LARGEST NUMBER
# ==========================================================


print("\n11. LARGEST NUMBER")
print("-" * 60)

num1 = 100
num2 = 250

largest = num1 if num1 > num2 else num2

print("First Number  :", num1)
print("Second Number :", num2)

print("Largest Number:", largest)


# ==========================================================
# 12. PRACTICAL EXAMPLE - VOTING ELIGIBILITY
# ==========================================================


print("\n12. VOTING ELIGIBILITY")
print("-" * 60)

age = 22

result = "Eligible to Vote" if age >= 18 else "Not Eligible to Vote"

print("Age    :", age)
print("Status :", result)


# ==========================================================
# 13. PRACTICAL EXAMPLE - STUDENT RESULT
# ==========================================================


print("\n13. STUDENT RESULT")
print("-" * 60)

student_name = "Rahul"

python_marks = 78
sql_marks = 82
excel_marks = 75

total = python_marks + sql_marks + excel_marks

average = total / 3

result = "Pass" if average >= 40 else "Fail"

print("Student Name :", student_name)

print("Python Marks :", python_marks)
print("SQL Marks    :", sql_marks)
print("Excel Marks  :", excel_marks)

print("Total Marks  :", total)
print("Average      :", average)

print("Result       :", result)


# ==========================================================
# 14. PRACTICAL EXAMPLE - EMPLOYEE BONUS
# ==========================================================


print("\n14. EMPLOYEE BONUS")
print("-" * 60)

employee_name = "Amit"

salary = 40000

experience = 3

eligible = salary <= 50000 and experience >= 2

bonus = salary * 0.10 if eligible else 0

total_salary = salary + bonus

print("Employee Name   :", employee_name)

print("Salary          :", salary)

print("Experience      :", experience)

print("Bonus Eligible  :", eligible)

print("Bonus           :", bonus)

print("Total Salary    :", total_salary)


# ==========================================================
# 15. PRACTICAL EXAMPLE - SHOPPING BILL
# ==========================================================


print("\n15. SHOPPING BILL")
print("-" * 60)

product = "Laptop"

price = 60000

quantity = 2

total = price * quantity

discount = total * 0.10 if total >= 100000 else 0

final_amount = total - discount

print("Product      :", product)

print("Price        :", price)

print("Quantity     :", quantity)

print("Total        :", total)

print("Discount     :", discount)

print("Final Amount :", final_amount)


# ==========================================================
# 16. USER INPUT PROGRAM
# ==========================================================


print("\n16. USER INPUT - SIMPLE CALCULATOR")
print("-" * 60)

num1 = float(input("Enter First Number  : "))

num2 = float(input("Enter Second Number : "))

print("\nAddition             :", num1 + num2)

print("Substraction         :", num1 - num2)

print("Multiplication       :", num1 * num2)

if num2 != 0:

    print("Division             :", num1 / num2)

    print("Floor Division       :", num1 // num2)

    print("Modulus              :", num1 % num2)

else:

    print("Division             : Cannot divide by zero")

    print("Floor Division       : Cannot divide by zero")

    print("Modulus              : Cannot divide by zero")


print("Power :", num1 ** num2)


# ==========================================================
# END
# ==========================================================


print("\n" + "=" * 60)

print("             PYTHON OPERATORS PROGRAM COMPLETED")

print("=" * 60)