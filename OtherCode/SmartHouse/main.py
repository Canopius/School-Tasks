class smartLight:
    def __init__(self, luminity, colour):
        self.luminity = clamp(luminity, 0, 1)
        self.colour = colour

    def changeLumity(self, newLuminity):
        self.luminity = clamp(newLuminity, 0, 1)

    def changeColour(self, newColour):
        self.colour = newColour

class smartBlind:
    def __init__(self, open):
        self.open = open

    def toggleOpen(self):
        self.open = not self.open

class smartHeating:
    def __init__(self, temp):
        self.temp = temp

    def changeTemp(self, newTemp)
        self.temp = newTemp

def main():
    a = smartBlind(True)
    b = smartLight(0.5, [255,255,255])
    c = smartBlind(True)
    d = smartBlind(False)

try:
    main()
except:
    print("An error has occured")