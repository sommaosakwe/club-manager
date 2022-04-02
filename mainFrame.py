from tkinter import *

class mainFrame(Frame):

    def addButton(self):
        f = Label(self, text="Hi")
        f.pack()

    def __init__(self, parent):
        Frame.__init__(self, parent, name="main")
        button = Button(self, text="Main Button", command=self.addButton)
        button.grid(row=0,column=1)
        button.pack()