products = ["Samsung Galaxy", "Shoes", "Laptop", "smart watch", "Shirt", "Headphones"]
s_products = list(filter(lambda product: product.lower().startswith("s"), products))
print(s_products)