try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

except ValueError:
    print("Invalid input. Please enter numbers only.")

else:
    print("Total price:", total)

finally:
    print("Thank you for shopping!")
