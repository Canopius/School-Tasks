import csv

x = 0

with open('uploadnums.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for index in range(0, len(row)):
                total = 0
                for i in range(0, len(row[index])):
                    total += int(row[index][i])
                if total == 13:
                    x += 1

print(x)