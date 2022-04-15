from tkinter import *
from tkinter import messagebox

from API.createAccount import createAccount

class memberCreateAccountFrame(Frame):
    def createAccount(self, username, password):
        if createAccount.createMember(username, password):
            messagebox.showinfo("Create Account","Account successfully created")
        else:
            messagebox.showwarning("Create Account","An account with that username already exists")

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="memberCreateAccount")
        self.config(width=1280, height=720)

        back = Button(self, text="Back to login", command=lambda: parent.switchFrame("memberLogin"))
        back.place(anchor='nw')

        container = Frame(self)
        heading = Label(container, text="Create Member Account", font=("Arial Bold", 25), pady=10)
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

        createAccount = Button(container, text="Create Account", command=lambda: self.createAccount(usernameF.get(), passwordF.get()))
        createAccount.pack(anchor='w',side=BOTTOM)
        
        container.place(relx=0.5, rely=0.33, anchor="center")