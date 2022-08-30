import csv
# https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
rows = []

# cat file.txt | nano

with open("grades.csv", 'r' ) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)


