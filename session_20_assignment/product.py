class Product:
    def __init__(self, price):
        self._price = price

    def display_price(self):
        print("Product price:", self._price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price


product1 = Product(500)
product1.display_price()
print("Current price:", product1.get_price())
product1.set_price(700)
print("Updated price:", product1.get_price())
