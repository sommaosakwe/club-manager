from tkinter import *

from API.login import login
from API.currentUser import currentUser

class treasurerLoginFrame(Frame):

    def login(self, parent, username, password):
        if (login.treasurerLogin(username, password)):
            currentUser.setCurrentUser("clubtreasurer")
            parent.switchFrame("treasurerContainer")
        else:
            Label(self, text="Incorrect login!").place(anchor='s',relx=0.5, rely=0.5)

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="treasurerLogin")
        self.config(width=1280, height=720)

        back = Button(self, text="Back to login choice", command=lambda: parent.switchFrame("loginChoice"))
        back.place(anchor='nw')

        container = Frame(self)
        heading = Label(container, text="TreasurerLogin", font=("Arial Bold", 25), pady=10)
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

        submit = Button(container, text="Login", command=lambda: self.login(parent, usernameF.get(), passwordF.get()))
        submit.pack(anchor='w',side=BOTTOM)
        container.place(relx=0.5, rely=0.33, anchor="center")

