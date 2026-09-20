def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")
    return name 

result = clean_brand_name("  oneplus-nord  ")
print(result)