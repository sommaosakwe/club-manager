from tkinter import *
from GUI.coachLoginFrame import coachLoginFrame
from GUI.mainFrame import mainFrame
from GUI.memberContainer import memberContainer
from GUI.memberLoginFrame import memberLoginFrame
from GUI.loginChoiceFrame import loginChoiceFrame
from GUI.treasurerLoginFrame import treasurerLoginFrame

class GUI:

    def __init__(self):
        self.main = Tk()
        self.currentFrame = None
        self.childrenFrames = {
            "main": mainFrame,
            "loginChoice": loginChoiceFrame,
            "memberLogin": memberLoginFrame,
            "coachLogin": coachLoginFrame,
            "treasurerLogin": treasurerLoginFrame,
            "memberContainer": memberContainer
        }

    def switchFrame(self, frameName):
        f = self.childrenFrames[frameName]
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = f(self)
        self.currentFrame.pack()

    def createMainWindow(self):
        self.main.title("Club Finances")

        w = 1280
        h = 720
        ws = self.main.winfo_screenwidth()
        hs = self.main.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.main.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.main.resizable(False,False)

        self.currentFrame = loginChoiceFrame(self)
        self.currentFrame.pack()
        self.main.mainloop()
    