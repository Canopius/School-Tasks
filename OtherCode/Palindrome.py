Word = input("Input word: ")
Word = Word.lower()
Word.replace(" ", "")
Reverse = Word[::-1]
if Reverse == Word:
    print("Yay")
else:
    print("Nay")