import csv

x = 0
largeVal = 0
smallVal = 999999999

def DigitSum(Num):
    total = 0
    for i in range(0, len(Num)):
        total += int(Num)
        
    if total == 13:
        x += 1

def Small(Num):
    global smallVal
    if smallVal >= Num:
        smallVal = Num
    
    return smallVal

def Large(Num):
    global largeVal
    if largeVal <= Num:
        largeVal = Num

    return largeVal

with open('uploadnums.csv') as CSVFile:
    CSVRead = csv.reader(CSVFile, delimiter=',')
    for row in CSVRead:
        for index in range(0, len(row)):
            DigitSum(row[index])
            Small(int(row[index]))
            Large(int(row[index]))    

print(("Digit Sum = 13: {}\nSmall: {}\nLarge: {}").format(x, smallVal, largeVal))