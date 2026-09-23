cart = int(input("Enter Flipkart cart value: "))
payment = input("Enter payment method: ")

if cart > 1000:
    if payment == "UPI":
        print("Eligible for 10% cashback")
    else:
        print("Eligible for 5% cashback")
else:
    print("No cashback")