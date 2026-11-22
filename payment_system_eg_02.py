# Example 2 – Payment System
# A practical example similar to payment processing used in applications.

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class NetBanking(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


upi = UPI()
card = CreditCard()
bank = NetBanking()

upi.pay(1500)
card.pay(2500)
bank.pay(5000)

# Here, every payment method must implement pay(), but each class defines its own payment behaviour.