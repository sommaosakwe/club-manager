from tkinter import *

class testFrame(Frame):

    def addButton(self):
        f = Label(self, text="Test Frame Behaviour")
        f.pack()

    def __init__(self, parent):
        Frame.__init__(self, parent, name="test")
        button = Button(self, text="Test Button", command=self.addButton)
        button.grid(row=0,column=1)
        button.pack()