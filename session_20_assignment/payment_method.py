from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentMethod):

    def pay(self, amount):
        print("Payment of", amount, "made using UPI")


class CreditCard(PaymentMethod):

    def pay(self, amount):
        print("Payment of", amount, "made using Credit Card")


upi = UPI()
upi.pay(1000)

card = CreditCard()
card.pay(2000)
