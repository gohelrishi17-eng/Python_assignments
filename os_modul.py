import os

files = os.listdir()

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        print(file)
