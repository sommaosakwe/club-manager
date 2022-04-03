from tkinter import *
from mainFrame import mainFrame
from testFrame import testFrame

class GUI:

    def __init__(self):
        self.main = Tk()
        self.currentFrame = None
        self.frames = {"main": mainFrame, "test": testFrame}

    def switchFrame(self, frameName):
        f = self.frames[frameName]
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = f(self)
        self.currentFrame.pack()

    def createMainWindow(self):
        self.main.title("Club Finances")
        self.main.geometry('1280x720')
        self.currentFrame = mainFrame(self)
        self.currentFrame.pack()
        self.main.mainloop()
    