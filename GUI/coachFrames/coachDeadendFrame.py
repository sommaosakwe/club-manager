from tkinter import *

class coachDeadendFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, name="memberNotifications")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        errorMessage = Label(self, text="Error: You are not registered in the club!\nPlease provide the treasurer with your username to be registered as a coach.")
        errorMessage.pack(side=TOP)