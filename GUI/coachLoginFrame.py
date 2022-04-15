from tkinter import *
from tkinter import messagebox

from API.login import login
from API.currentUser import currentUser

class coachLoginFrame(Frame):

    def login(self, parent, username, password):
        if (login.coachLogin(username, password)):
            currentUser.setCurrentUser(username)
            parent.switchFrame("coachContainer")
        else:
            messagebox.showwarning("Login Error","Incorrect login")

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="coachLogin")
        self.config(width=1280, height=720)

        back = Button(self, text="Back to login choice", command=lambda: parent.switchFrame("loginChoice"))
        back.place(anchor='nw')

        container = Frame(self)
        heading = Label(container, text="Coach Login", font=("Arial Bold", 25), pady=10)
        heading.pack(side=TOP)

        usernameS = Frame(container)
        usernameL = Label(usernameS, text="Username:")
        usernameL.pack(anchor='w',side=LEFT)
        usernameF = Entry(usernameS)
        usernameF.pack(anchor='w',side=LEFT,fill=X,expand=1)
        usernameS.pack(anchor='w',side=TOP,fill=X,expand=1)

        passwordS = Frame(container)
        passwordL = Label(passwordS, text="Password:")
        passwordL.pack(anchor='w',side=LEFT)
        passwordF = Entry(passwordS)
        passwordF.pack(anchor='w',side=LEFT,fill=X,expand=1)
        passwordS.pack(anchor='w',side=TOP,fill=X,expand=1)

        buttonF = Frame(container)
        submit = Button(buttonF, text="Login", command=lambda:self.login(parent, usernameF.get(), passwordF.get()))
        submit.pack(side=LEFT)
        createAccount = Button(buttonF, text="Create Account", command=lambda: parent.switchFrame("coachCreateAccount"))
        createAccount.pack(side=RIGHT)
        buttonF.pack(side=BOTTOM,fill=X,expand=1)

        container.place(relx=0.5, rely=0.33, anchor="center")
