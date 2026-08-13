# *Employee Payroll System*

# Objective

# Create a payroll system using variables.

# --------------------------
# Employee Payroll System
# --------------------------


# Use one Global Variable: company_name

company_name = "Syntova"

# Employee details : Employee Name, Employee ID, Department, Designation

employee_id = 101

employee_name = "Atharva Satpute"

department = "Data"

designation = "Data Engineer"


# Store : Basic Salary, HRA, DA, Bonus (Multiple Assignment)

basic_salary, hra, da, bonus = 50000, 10000, 7500, 5000


# Calculate: Gross Salary

# Formula :

gross_salary = basic_salary + hra + da + bonus


# Swapping two variables : HRA and Bonus

# Before Swapping : 

print("Before Swapping")

print(f"HRA = {hra}")

print(f"Bonus = {bonus}")

# Swapping variables

hra, bonus = bonus, hra

# After Swapping :

print("\nAfter Swapping")

print(f"HRA = {hra}")

print(f"Bonus = {bonus}")
 

print("\n=========================")
print(" EMPLOYEE PAYROLL SYSTEM ")
print("=========================")


# Display output using f-strings.

# Display Employee Information :

print(f"Company Name : {company_name}")

print(f"Employee ID : {employee_id}")

print(f"Employee Name : {employee_name}")

print(f"Department : {department}")

print(f"Designation : {designation}")


print("\n------ Salary Details ------")

print(f"Salary : {basic_salary}")

print(f"HRA : {hra}")

print(f"DA : {da}")

print(f"Bonus : {bonus}")


print("\n------ Gross Salary ------")

print(f"Gross Salary : {gross_salary}")


print("\n-------- Thank You --------")