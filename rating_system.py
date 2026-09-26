try:
    reviews = int(input("Enter number of reviews: "))
    stars = int(input("Enter total stars: "))
    
    average = stars / reviews
    print("Average rating:", average)

except ValueError:
    print("Error: Please enter numbers only")
