class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Available Balance:", self.__balance)


atm1 = ATM(70000)

atm1.check_balance()

atm1.deposit(6000)
atm1.check_balance()

atm1.withdraw(7000)
atm1.check_balance()

atm1.withdraw(20000)