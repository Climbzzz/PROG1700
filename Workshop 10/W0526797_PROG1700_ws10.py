import csv
with open("results.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Operation", "Result"])