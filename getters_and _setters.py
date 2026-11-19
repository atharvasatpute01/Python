# 3. Getters and Setters

# We use getter and setter methods to read and update private variables.
# - Getter: Retrieves the value.
# - Setter: Updates the value after validation.


class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):

        if amount > 0:
            self.__salary = amount
            print("Salary Updated Successfully")


        else:
            print("Invalid Salary")


emp = Employee(30000)

print("Current Salary:", emp.get_salary())

emp.set_salary(50000)

print("Updated Salary:", emp.get_salary())

emp.set_salary(-1000)