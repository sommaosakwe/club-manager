from tkinter import *

class loginChoiceFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="loginChoice")
        self.config(width=1280, height=720)

        choices = Frame(self)

        heading = Label(choices, text="Login as:", font=("Arial Bold", 25), pady=10)
        heading.pack(side=TOP)

        buttonC = Button(choices, text="Coach", command=lambda: parent.switchFrame("coachLogin"))
        buttonC.pack(side=RIGHT)

        buttonM = Button(choices, text="Member", command=lambda: parent.switchFrame("memberLogin"))
        buttonM.pack(side=RIGHT)

        buttonT = Button(choices, text="Treasurer", command=lambda: parent.switchFrame("treasurerLogin"))
        buttonT.pack(side=RIGHT)

        choices.place(relx=0.5, rely=0.33, anchor="center")