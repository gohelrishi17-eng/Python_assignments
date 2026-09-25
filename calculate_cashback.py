def calculate_cashback(amount, cashback_rate=0.05):
    cashback = amount * cashback_rate
    return cashback

zomato_cashback =  calculate_cashback(500)
print("zomato_cashback:", zomato_cashback)

flipcart_cashback = calculate_cashback(2000, 0.07)
print("flipcart_cashback:", flipcart_cashback)