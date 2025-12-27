import csv

pass_count = 0
fail_count = 0

with open("python-week1/result.csv") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader :
        result = row[2]

        if result == "Pass" :
            pass_count += 1
        else :
            fail_count += 1

print("Pass : ", pass_count)
print("Fail : ", fail_count)

total = pass_count + fail_count
print("Total : ", total)
print("Pass rate : ", pass_count / total)