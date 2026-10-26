# Simple ATM Using Functions


def check_balance(balance):
    print("Current Balance:", balance)


def deposit(balance):
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully.")
    else:
        print("Invalid amount.")

    return balance


def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance = balance - amount
        print("Please collect your cash.")
        print("Withdrawal successful.")

    return balance


def atm():
    
    balance = 10000

    while True:

        print("\n====================")
        print("       ATM")
        print("====================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("====================")

        choice = input("Enter your choice: ")

        if choice == "1":

            check_balance(balance)

        elif choice == "2":

            balance = deposit(balance)

        elif choice == "3":

            balance = withdraw(balance)

        elif choice == "4":

            print("Thank you for using the ATM.")
            break

        else:

            print("Invalid choice. Please try again.")


# Start ATM
atm()