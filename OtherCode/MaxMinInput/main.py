def CheckNumbers(No, Lower, Upper):
    if max(min(No, Upper), Lower) == No:
        return True
    else:
        return False
    
def main():
    Total = 0
    for i in range(1, 11):
        Number = int(input("Number: "))
        Lower = int(input("Lower: "))
        Upper = int(input("Upper: "))
        if Lower > Upper:
            print("\nLower must be smaller than upper\n")
            continue
        Total = Total + Number
        if CheckNumbers(Number, Lower, Upper):
            break
        print("\n")
    print(Total)

try:
    main()
except:
    print("An error has occured")