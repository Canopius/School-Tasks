import string, math

def noSpaces(a):
    return a.count(' ')

count = lambda l1,l2: sum([1 for x in l1 if x in l2])

def encode(a):
    x = []

    

    return x

foo = input("Enter an input: ")
print(noSpaces(foo))
print(count(foo,set(string.punctuation)))
print(encode(foo))
