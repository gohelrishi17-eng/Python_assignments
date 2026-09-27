def cashback_generator(transactions):
    for amount in transactions:
        cashback = amount * 0.05
        yield cashback


transactions = [100, 500, 1000, 250, 800]

cashback = cashback_generator(transactions)

for value in cashback:
    print("Cashback:", value)
