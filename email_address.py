import re

text = "Great food! Contact zomato@gmail.com or rahul123@yahoo.com for details. Also try abc@outlook.com."
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(pattern, text)
print(emails)