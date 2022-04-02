from tkinter import *
from mainFrame import mainFrame
from testFrame import testFrame

class GUI:

    currentFrame = None

    def __init__(self):
        self.main = Tk()

    def switchFrames(self):
        if self.currentFrame.winfo_name() == "main":
            self.currentFrame.pack_forget()
            self.currentFrame = testFrame(self.main)
            self.currentFrame.pack()
        elif self.currentFrame.winfo_name() == "test":
            self.currentFrame.pack_forget()
            self.currentFrame = mainFrame(self.main)
            self.currentFrame.pack()

    def createMainWindow(self):
        self.main.title("Club Finances")
        self.main.geometry('1280x720')
        b = Button(self.main, text = "Switch Frames", command=self.switchFrames)
        b.pack()
        self.currentFrame = mainFrame(self.main)
        self.currentFrame.pack()
        self.main.mainloop()
    