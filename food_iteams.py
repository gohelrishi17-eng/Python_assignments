foods = ["Pizza", "Burger", "Pasta", "Sandwich"]
prices = [250, 150, 200, 300]

for food, price in zip(foods, prices):
    print(food, "-", "₹", price)
