class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def update_salary(self, amount):

        if amount >= 0:
            self.__salary = amount
            print("Salary updated successfully.")

        else:
            print("Salary cannot be negative!")

e1 = Employee("Atharva", 50000)

print("Employee Name:", e1.name)

print("Current Salary:", e1.get_salary())

e1.update_salary(40000)

print("Updated Salary:", e1.get_salary())

e1.update_salary(-200)