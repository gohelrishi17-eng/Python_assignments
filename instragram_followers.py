followers = [120, 1500, 23000, 800, 45000]

for count in followers:

    if count < 1000:
        print("Micro")

    elif count <= 10000:
        print("Influencer")

    else:
        print("Celebrity")