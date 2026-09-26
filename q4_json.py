import json

file = open("user_profile.json", "r")

data = json.load(file)

print("Username:", data["username"])
print("Followers:", data["followers"])

file.close()
