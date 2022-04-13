from tkinter import *

class memberDeadendFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, name="memberNotifications")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        back = Button(self, text="Logout", command=lambda: exit(0))
        back.pack(anchor='ne',side=RIGHT)

        errorMessage = Label(self, text="Error: You are not registered in the club!\nPlease provide a coach with your username to be registered.")
        errorMessage.pack(side=TOP)