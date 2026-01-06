import csv

with open("python-week1/data.csv") as f:
    reader = csv.reader(f)

    for row in reader :
        # print(row)
        name = row[0]
        score = row[1]
        print(name, score)