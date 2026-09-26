try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter numbers only")


# I learned that AI can handle multiple types of errors using saparate except blocks    
