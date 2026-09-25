def get_delivery_charge(amount, city="ahemdabad"):
    if city == "ahemdabad":
        return 30
    else:
        return 50

print(get_delivery_charge(200))
print(get_delivery_charge(200, "dilhi"))    