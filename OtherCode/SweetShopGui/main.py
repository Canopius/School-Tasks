import tkinter as tk
import uuid
import hashlib

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
        ShowSignUp(root)
        

    def verifyCreds(self):
        print(self.userInput.get())
        print(self.passwordInput.get())


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

        
def ShowSignUp(oldRoot):
    root = tk.Tk()
    app = SignUp(master=root)
    app.mainloop()

def ShowLogin():
    for index in range(0,len(allWidgets)):
        allWidgets[index].destroy()

    root = tk.Tk()
    app = LoginApplication(master=root)
    app.mainloop()

root = tk.Tk()
app = LoginApplication(master=root)
app.mainloop()