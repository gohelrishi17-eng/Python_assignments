import re

text = "olx: sofa $5000, contact 8735628652 or 9824446323. code 12345."

pattern = r"\b[789]\d{9}\b"
phone_numbers = re.findall(pattern, text)
print(phone_numbers)