import tkinter as tk
import uuid
import hashlib
import csv

OpenWindow = None

class Application(tk.Frame):

    def createLabel(self, text, location):
        label = tk.Label(self, text=text)
        label.pack(side=location)
        return label

    def createEntry(self, text, location):
        entry = tk.Entry(self)
        entry.pack(side=location)
        return entry

    def createButton(self, text, location):
        button = tk.Button(self, text=text)
        button.pack(side=location)
        return button

class ShopApplication(Application):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.Stock = {}

        self.SubTotal = 0

        with open('stock.csv', 'r', newline='')  as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for i, line in enumerate(reader):

                self.Stock[line[i]] = []

                sweetName = self.createLabel(line[0], "top")
                sweetPrice = self.createLabel("£" + line[1], "top")
                sweetQty = self.createEntry("Qty", "top")

                AddToCart = self.createButton("Add To Cart", "top")
                AddToCart["command"] = self.AddToCart

                self.Stock[line[i]].append(sweetName)
                self.Stock[line[i]].append(sweetPrice)
                self.Stock[line[i]].append(sweetQty)
                self.Stock[line[i]].append(AddToCart)

        self.SubTotalLabel = self.createLabel("Sub-Total: £0.00", "top")

    def AddToCart():
        print("Nothing yet")


class LoginApplication(Application):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        OpenWindow = self.master

        self.userLabel = self.createLabel("Username", "top")
        self.userInput = self.createEntry("",  "top")

        self.passwordLabel = self.createLabel("Password", "top")
        self.passwordInput = self.createEntry("",  "top")
        self.passwordInput["show"] = '*'

        self.login = self.createButton("Login", "top")
        self.login["command"] = self.verifyCreds

        self.signUp = self.createButton("Sign Up", "top")
        self.signUp["command"] = self.signUpActivated

    def signUpActivated(self):
        ShowSignUp()
        
    def verifyCreds(self):
        with open('creds.csv', 'r', newline='')  as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for i, line in enumerate(reader):
                if line[0] == self.userInput.get():
                    if CheckPassword(line[1],self.passwordInput.get()):
                        ShowShop()
                        return True
                    
        print("Username not found")
        return False
        


class SignUp(Application):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        OpenWindow = self.master

        self.userLabel = self.createLabel("Username", "top")
        self.userInput = self.createEntry("",  "top")

        self.passwordLabel = self.createLabel("Password", "top")
        self.passwordInput = self.createEntry("",  "top")
        self.passwordInput["show"] = '*'

        self.confirmPasswordLabel = self.createLabel("Confirm Password", "top")
        self.confirmPasswordInput = self.createEntry("",  "top")
        self.confirmPasswordInput["show"] = '*'

        self.createAccount = self.createButton("Create Account", "top")
        self.createAccount["command"] = self.storeDetails

        self.login = self.createButton("Login", "top")
        self.login["command"] = self.loginActivated

    def loginActivated(self):
        ShowLogin()

    def storeDetails(self):
        if self.passwordInput.get() != self.confirmPasswordInput.get() or len(self.userInput.get()) <= 0 or len(self.passwordInput.get()) <= 0:
            return False

        hashedPassword = HashPassword(self.passwordInput.get())

        with open('creds.csv', 'a', newline='') as csvfile:
            credWrite = csv.writer(csvfile, delimiter=',')
            credWrite.writerow([self.userInput.get()] + [hashedPassword])


def ShowSignUp():
    root = tk.Tk()
    app = SignUp(master=root)
    app.mainloop()

def ShowLogin():
    root = tk.Tk()
    app = LoginApplication(master=root)
    app.mainloop()

def ShowShop():
    root = tk.Tk()
    app = ShopApplication(master=root)
    app.mainloop()

def HashPassword(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def CheckPassword(hashedPassword, userPassword):
    password, salt = hashedPassword.split(':')
    return password == hashlib.sha256(salt.encode() + userPassword.encode()).hexdigest()

root = tk.Tk()
app = LoginApplication(master=root)
app.mainloop()
