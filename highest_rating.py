ratings = ["4.5", "3.0", "5", "4.2"]
float_ratings = []

for rating in ratings:
    float_ratings.append(float(rating))

highest = max(float_ratings)

print("ratings:", float_ratings)
print("highest rating:", highest)