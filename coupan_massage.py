def format_coupon_message(username, discount=10):
    message = f"Hi {username}, you get {discount}% off!"
    return message

print(format_coupon_message("Rahul", 20))
print(format_coupon_message("Rishi"))   