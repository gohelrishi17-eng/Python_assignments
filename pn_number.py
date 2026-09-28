import re

text = "My phone number is 9876543210."
masked_text = re.sub(r"\d{6}(?=\d{4})", "******", text)
print(masked_text)