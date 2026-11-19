class ATM:
    def __init__(self, account_holder, balance):

        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Deposit Successful")

        else:
            print("Invalid Amount")

    def withdraw(self, amount):

        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal Successful")

        else:
            print("Insufficient Balance")

    def check_balance(self):

        print("Amount Holder:", self.account_holder)
        print("Available Balance:", self.__balance)

atm = ATM("Rahul", 10000)

atm.check_balance()

atm.deposit(5000)

atm.withdraw(3000)

atm.check_balance()