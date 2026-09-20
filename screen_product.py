products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

cleaned_products = []

for name in products:
    name = name.strip()
    name = name.replace("-", " ")
    name = name.title()
    cleaned_products.append(name)

print(cleaned_products)