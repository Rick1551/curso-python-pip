import csv

with open("app/se.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        print("****" * 5)
        print("row")

