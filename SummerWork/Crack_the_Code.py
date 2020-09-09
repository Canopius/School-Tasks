import random

# Constants
codeLen = 4

def genCode():
    code = []
    for i in range(0,codeLen):
        code.append(random.randint(1,9))

    return code

def usrInput():
    x = input("\nPlease enter the code: ")
    if len(x) == codeLen and int(x):
        return x
    else:
        return False

def checkCode(compCode, usrCode):
    usrCode = list(usrCode)
    right = 0
    print("\n")
    for i in range(0,codeLen):
        if compCode[i] == int(usrCode[i]):
            print("Digit", i + 1, " is just right")
            right += 1
        elif compCode[i] < int(usrCode[i]):
            print("Digit", i + 1, " is too large")
        else:
            print("Digit", i + 1, " is too small")

    if right == 4:
        return True

def main():
    correct = False
    compCode = genCode() # Returns a table

    while not (correct):
        usrCode = usrInput()
        if not (usrCode):
            print("\nYour input is not the correct length or correct type, please try again\n")
            pass
        elif (checkCode(compCode, usrCode)):
            print("\nYou cracked the code!\n")
            correct = True
            return True

try:
    main()
except:
    print("An error has occured, please try again.")
