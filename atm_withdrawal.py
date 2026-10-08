balance = 10000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise Exception("Amount must be greater than zero")

    if amount > balance:
        raise Exception("Insufficient balance")

    balance = balance - amount

    print("Withdrawal successful")
    print("Remaining balance:", balance)

except ValueError:
    print("Please enter a valid amount.")

except Exception as e:
    print("Transaction failed:", e)