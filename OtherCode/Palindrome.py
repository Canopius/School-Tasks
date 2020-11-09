vowel = ["a","e","i","o","u"]
cons = ["b","c","d","f","g","g","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
findOccurrences = lambda s, ch : [i for i, letter in enumerate(s) if letter in (b for b in ch)]
Word = input("Input word: ").lower().replace(" ", "")
print("There are: {} vowel(s) and {} consonant(s)".format(len(findOccurrences(Word,vowel)), len(findOccurrences(Word,cons))))
Reverse = Word[::-1]
x = lambda a, b: a == b
print(x(Word, Reverse))
    