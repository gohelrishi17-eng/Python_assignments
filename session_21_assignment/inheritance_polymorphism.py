class Product:
    def get_discount(self):
        return 0


class Electronics(Product):
    def get_discount(self):
        return 10


product = Product()
electronics = Electronics()

print("Product discount:", product.get_discount())
print("Electronics discount:", electronics.get_discount())


class FoodOrder:
    def calculate_total(self, base_price):
        return base_price


class ZomatoOrder(FoodOrder):
    def calculate_total(self, base_price):
        return base_price + (base_price * 0.05)


order = FoodOrder()
zomato_order = ZomatoOrder()

print("Food Order Total:", order.calculate_total(1000))
print("Zomato Order Total:", zomato_order.calculate_total(1000))


class Influencer:
    def bonus(self):
        return 2000


class BrandManager:
    def bonus(self):
        return 5000


def show_bonus(employee):
    print("Bonus:", employee.bonus())


influencer = Influencer()
brand_manager = BrandManager()

show_bonus(influencer)
show_bonus(brand_manager)


class User:
    def get_status(self):
        return "active"


class PremiumUser(User):
    def get_status(self):
        return "premium"


user = User()
premium_user = PremiumUser()

print("User status:", user.get_status())
print("Premium User status:", premium_user.get_status())
