prices = ['199.99', '299.50', '150']
float_prices = []

for price in prices:
    float_prices.append(float(price))

total = sum(float_prices)

print("cart_price:",float_prices)
print("total cart value:",total)