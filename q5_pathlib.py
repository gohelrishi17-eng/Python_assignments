from pathlib import Path

file = Path("zomato_orders.json")

if file.exists():
    print("zomato_orders.json file found")
else:
    print("zomato_orders.json file not found")
