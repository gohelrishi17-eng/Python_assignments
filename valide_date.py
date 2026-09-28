import re

def check_date(text):
    result = re.search(r"\b\d{2}/\d{2}/\d{4}\b", text)
    return result is not None

print(check_date("Meeting on 25/06/2024"))
print(check_date("Meeting on 25-06-2024"))