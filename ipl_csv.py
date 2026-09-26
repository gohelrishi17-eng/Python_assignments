import csv

file = open("ipl_matches.csv", "r")

reader = csv.DictReader(file)

for row in reader:
    print(row["Winner"])

file.close()    
