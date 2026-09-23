followers = int(input("Enter Followers:"))

if followers < 10000:
    print("Micro influencer")
elif followers <= 100000:
    print("Rising star")
else:
    print("celebrity")    