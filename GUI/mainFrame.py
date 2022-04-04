from tkinter import *

class mainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="main")
        button = Button(self, text="Go to Test Frame", command=lambda: parent.switchFrame("test"))
        button.grid(row=0,column=1)
