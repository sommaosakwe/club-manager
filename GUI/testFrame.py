from tkinter import *

class testFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="test")
        button = Button(self, text="Go to Main Frame", command=lambda: parent.switchFrame("loginChoice"))
        button.grid(row=0,column=1)
        button.pack()