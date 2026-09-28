import re

order_id = "My Flipkart order is OD123456789012345000."
pattern = r"\bOD\d{18}\b"
result = re.search(pattern, order_id)

if result:
    print("Valid Flipkart Order ID:", result.group())
else:
    print("Order ID not found")