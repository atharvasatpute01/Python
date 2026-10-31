# Employee Salary Calculator with PF


def calculate_hra(basic_salary):
    hra = basic_salary * 0.20
    return hra


def calculate_pf(basic_salary):
    pf = basic_salary * 0.12
    return pf


def calculate_salary(basic_salary):

    hra = calculate_hra(basic_salary)

    gross_salary = basic_salary + hra

    pf = calculate_pf(basic_salary)

    net_salary = gross_salary - pf

    return hra, gross_salary, pf, net_salary


def display_salary(name, employee_id, basic_salary):

    hra, gross_salary, pf, net_salary = calculate_salary(basic_salary)

    print("\n====================================")
    print("       EMPLOYEE SALARY SLIP")
    print("====================================")

    print("Employee Name :", name)
    print("Employee ID   :", employee_id)

    print("------------------------------------")

    print("Basic Salary  : ₹", basic_salary)
    print("HRA (20%)     : ₹", hra)
    print("Gross Salary  : ₹", gross_salary)

    print("------------------------------------")

    print("Employee PF   : ₹", pf)
    print("Net Salary    : ₹", net_salary)

    print("====================================")


def employee_salary():

    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")

    basic_salary = float(
        input("Enter basic salary: ₹")
    )

    if basic_salary <= 0:
        print("Invalid salary.")
        return

    display_salary(
        name,
        employee_id,
        basic_salary
    )


# Start program
employee_salary()